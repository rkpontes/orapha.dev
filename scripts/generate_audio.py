#!/usr/bin/env python3
"""
Script para gerar áudio dos artigos do blog usando TTS.
Suporta múltiplos backends: macOS say (nativo), Fish Speech (quando instalado), etc.
"""

import os
import re
import sys
import glob
import subprocess
from pathlib import Path
from datetime import datetime

# Configurações
CONTENT_DIR = Path("/Users/raphaelpontes/Documents/Projetos/orapha_dev/content")
AUDIO_DIR = Path("/Users/raphaelpontes/Documents/Projetos/orapha_dev/static/audio")
BLOG_PATTERN = "**/index.md"

def extract_text_from_markdown(file_path):
    """Extrai o texto limpo de um arquivo markdown."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove o frontmatter (cabeçalho entre ---)
    content = re.sub(r'^---\n.*?---\n', '', content, flags=re.DOTALL)
    
    # Remove links markdown [texto](url) -> texto
    content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
    
    # Remove imagens markdown ![alt](url)
    content = re.sub(r'!\[([^\]]*)\]\([^)]+\)', '', content)
    
    # Remove blocos de código
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    content = re.sub(r'`[^`]+`', '', content)
    
    # Remove hashtags de títulos # Titulo -> Titulo
    content = re.sub(r'^#+\s*', '', content, flags=re.MULTILINE)
    
    # Remove listas markdown (* - 1.)
    content = re.sub(r'^[\*\-\+]\s*', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\d+\.\s*', '', content, flags=re.MULTILINE)
    
    # Remove formatação **texto** *texto* __texto__
    content = re.sub(r'\*\*([^*]+)\*\*', r'\1', content)
    content = re.sub(r'\*([^*]+)\*', r'\1', content)
    content = re.sub(r'__([^_]+)__', r'\1', content)
    content = re.sub(r'_([^_]+)_', r'\1', content)
    
    # Remove blocos de citação >
    content = re.sub(r'^>\s*', '', content, flags=re.MULTILINE)
    
    # Remove linhas horizontais
    content = re.sub(r'^---+$', '', content, flags=re.MULTILINE)
    
    # Remove HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    
    # Remove linhas vazias excessivas
    content = re.sub(r'\n\n+', '\n\n', content)
    
    # Remove espaços no início e fim
    content = content.strip()
    
    return content

def get_article_slug(file_path):
    """Extrai o slug do artigo a partir do path."""
    # Path: content/2026/05/09/slug/index.md
    parts = Path(file_path).parts
    # Encontrar o slug (diretório pai do index.md)
    if 'index.md' in parts:
        idx = parts.index('index.md')
        if idx > 0:
            return parts[idx - 1]
    return None

def generate_audio_say(text, output_path):
    """Gera áudio usando o comando say do macOS (100% offline)."""
    # O say do macOS suporta português brasileiro com a voz Luciana
    # Primeiro, vamos verificar se a voz está disponível
    
    # Criar arquivo de texto temporário (say tem limite de caracteres na linha de comando)
    temp_txt = output_path.with_suffix('.txt')
    with open(temp_txt, 'w', encoding='utf-8') as f:
        f.write(text)
    
    try:
        # Usar a voz Luciana (PT-BR) se disponível, senão usar a padrão
        aiff_path = output_path.with_suffix('.aiff')
        cmd = ['say', '-f', str(temp_txt), '-o', str(aiff_path)]
        
        # Verificar se a voz Luciana existe
        result = subprocess.run(['say', '-v', '?'], capture_output=True, text=True)
        if 'Luciana' in result.stdout:
            cmd.extend(['-v', 'Luciana'])
        
        subprocess.run(cmd, check=True)
        
        # Converter para MP3 usando ffmpeg
        mp3_path = output_path.with_suffix('.mp3')
        subprocess.run([
            'ffmpeg', '-y', '-i', str(aiff_path),
            '-codec:a', 'libmp3lame',
            '-qscale:a', '0',  # Qualidade máxima (0-9, onde 0 é melhor)
            str(mp3_path)
        ], check=True, capture_output=True)
        
        # Remover arquivo aiff original
        aiff_path.unlink()
        
        # Remover arquivo temporário
        temp_txt.unlink()
        
        return mp3_path
        
    except Exception as e:
        print(f"Erro ao gerar áudio: {e}")
        # Limpar arquivos temporários em caso de erro
        if temp_txt.exists():
            temp_txt.unlink()
        aiff_temp = output_path.with_suffix('.aiff')
        if aiff_temp.exists():
            aiff_temp.unlink()
        return None

def split_text_into_chunks(text, max_chars=1000):
    """Divide o texto em chunks menores para processamento."""
    chunks = []
    current_chunk = ""
    
    # Dividir por frases (pontos seguidos de espaço)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= max_chars:
            current_chunk += sentence + " "
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

def process_article(md_file):
    """Processa um arquivo markdown e gera o áudio."""
    slug = get_article_slug(md_file)
    if not slug:
        print(f"Não foi possível extrair slug de: {md_file}")
        return None
    
    # Verificar se o áudio já existe e é mais recente que o markdown
    audio_path = AUDIO_DIR / f"{slug}.mp3"
    
    if audio_path.exists():
        audio_mtime = audio_path.stat().st_mtime
        md_mtime = md_file.stat().st_mtime
        
        if audio_mtime > md_mtime:
            print(f"Áudio já existe e está atualizado: {audio_path.name}")
            return audio_path
    
    print(f"Processando: {slug}")
    
    # Extrair texto
    text = extract_text_from_markdown(md_file)
    
    if not text or len(text.strip()) < 100:
        print(f"Texto muito curto ou vazio: {slug}")
        return None
    
    # Limitar tamanho do texto (primeiros 5000 caracteres para não ficar muito longo)
    # Você pode ajustar isso conforme necessário
    text = text[:5000]
    
    # Gerar áudio
    print(f"Gerando áudio para: {slug} ({len(text)} caracteres)")
    
    temp_aiff = AUDIO_DIR / f"{slug}.aiff"
    result = generate_audio_say(text, temp_aiff)
    
    if result:
        print(f"✓ Áudio gerado: {result.name}")
        return result
    else:
        print(f"✗ Falha ao gerar áudio para: {slug}")
        return None

def main():
    """Função principal."""
    # Criar diretório de áudio se não existir
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    
    # Encontrar todos os artigos
    articles = list(CONTENT_DIR.glob(BLOG_PATTERN))
    
    print(f"Encontrados {len(articles)} artigos")
    print(f"Diretório de áudio: {AUDIO_DIR}")
    print("-" * 60)
    
    # Processar cada artigo
    processed = 0
    failed = 0
    
    for i, article in enumerate(articles, 1):
        print(f"\n[{i}/{len(articles)}]", end=" ")
        result = process_article(article)
        if result:
            processed += 1
        else:
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Processamento concluído!")
    print(f"Sucesso: {processed}")
    print(f"Falhas: {failed}")
    print(f"Total: {len(articles)}")

if __name__ == "__main__":
    main()
