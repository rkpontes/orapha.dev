#!/usr/bin/env python3
"""
Script para gerar áudio dos artigos do blog usando TTS.
Suporta múltiplos backends: macOS say (nativo), Fish Speech (quando instalado), etc.

Uso:
    python scripts/generate_audio.py
    python scripts/generate_audio.py --slug meu-post
    python scripts/generate_audio.py --force
    python scripts/generate_audio.py --limit 5
    python scripts/generate_audio.py --dry-run
    python scripts/generate_audio.py --verbose
"""

import re
import sys
import subprocess
import argparse
import logging
from pathlib import Path

# Tenta importar bibliotecas opcionais
try:
    from tqdm import tqdm
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False
    tqdm = None

try:
    from mutagen.mp3 import MP3  # type: ignore[import]
    from mutagen.id3 import TIT2, TALB, TPE1, TDRC  # type: ignore[import]
    HAS_MUTAGEN = True
except ImportError:
    HAS_MUTAGEN = False

# Configurações
CONTENT_DIR = Path("/Users/raphaelpontes/Documents/Projetos/orapha_dev/content")
AUDIO_DIR = Path("/Users/raphaelpontes/Documents/Projetos/orapha_dev/static/audio")
BLOG_PATTERN = "**/index.md"


def setup_logging(verbose=False):
    """Configura o sistema de logging estruturado."""
    level = logging.DEBUG if verbose else logging.INFO

    # Configura formato das mensagens
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )

    # Configura handler para console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # Configura logger raiz
    logger = logging.getLogger()
    logger.setLevel(level)
    logger.handlers = []  # Limpa handlers anteriores
    logger.addHandler(console_handler)

    return logger


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


def extract_frontmatter(file_path):
    """Extrai metadados do frontmatter (título, data, autor, etc)."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    frontmatter = {}

    # Tenta extrair frontmatter entre ---
    match = re.match(r'^---\n(.*?)---\n', content, re.DOTALL)
    if match:
        front_text = match.group(1)

        # Extrai campos comuns
        title_match = re.search(r'^title:\s*(.+)$', front_text, re.MULTILINE)
        if title_match:
            frontmatter['title'] = title_match.group(1).strip().strip('"\'')

        date_match = re.search(r'^date:\s*(.+)$', front_text, re.MULTILINE)
        if date_match:
            frontmatter['date'] = date_match.group(1).strip()

        author_match = re.search(r'^author:\s*(.+)$', front_text, re.MULTILINE)
        if author_match:
            frontmatter['author'] = author_match.group(1).strip()
        else:
            frontmatter['author'] = "Raphael Pontes"  # Autor padrão

    return frontmatter


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


# ============================================================================
# SISTEMA DE BACKENDS TTS (Text-to-Speech)
# ============================================================================
#
# O código está estruturado para facilitar a adição de múltiplos backends TTS.
# Cada backend é uma função que segue a mesma interface:
#   - Entrada: texto (str), output_path (Path), metadata (dict, opcional)
#   - Saída: Path do arquivo gerado ou None em caso de erro
#
# Backends implementados:
# - say: macOS say (nativo, offline)
# - edge: Microsoft Edge TTS (gratuito, online, voz natural PT-BR)
#
# Exemplos de backends futuros:
# - fish_speech: Modelo de voz neural local (https://github.com/fishaudio/fish-speech)
# - openai_tts: API da OpenAI (requer chave de API)
# - elevenlabs: API ElevenLabs (requer chave de API)
# - piper: TTS local rápido e leve (https://github.com/rhasspy/piper)
#
# Para adicionar um novo backend:
# 1. Criar função generate_audio_<backend>(text, output_path, metadata=None)
# 2. Adicionar na função get_backend_function() para mapear nome -> função
# 3. Passar --backend <nome> via linha de comando
# ============================================================================

def generate_audio_say(text, output_path, metadata=None):
    """
    Backend: macOS say (nativo, offline).

    Usa o comando 'say' do macOS que já vem instalado.
    Converte primeiro para AIFF e depois para MP3 via ffmpeg.
    """
    logger = logging.getLogger()

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
            logger.debug("Usando voz Luciana (PT-BR)")

        logger.debug(f"Executando: {' '.join(cmd)}")
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

        logger.debug(f"Áudio gerado: {mp3_path}")

        # Adicionar metadados ID3 se disponível
        if HAS_MUTAGEN and metadata:
            add_id3_metadata(mp3_path, metadata)

        return mp3_path

    except Exception as e:
        logger.error(f"Erro ao gerar áudio: {e}")
        return None
    finally:
        # Limpar arquivos temporários
        if temp_txt.exists():
            temp_txt.unlink()
        aiff_temp = output_path.with_suffix('.aiff')
        if aiff_temp.exists():
            aiff_temp.unlink()


def add_id3_metadata(mp3_path, metadata):
    """
    Adiciona metadados ID3 ao arquivo MP3.

    Campos suportados:
    - TIT2: Título
    - TALB: Álbum (usado para categoria/site)
    - TPE1: Artista/Autor
    - TDRC: Data de gravação
    """
    try:
        audio = MP3(mp3_path)

        # Adiciona tag ID3 se não existir
        if audio.tags is None:
            audio.add_tags()

        # Define metadados
        if 'title' in metadata:
            audio.tags['TIT2'] = TIT2(encoding=3, text=metadata['title'])

        if 'author' in metadata:
            audio.tags['TPE1'] = TPE1(encoding=3, text=metadata['author'])

        # Usa 'orapha.dev' como álbum/categoria
        audio.tags['TALB'] = TALB(encoding=3, text="orapha.dev")

        if 'date' in metadata:
            audio.tags['TDRC'] = TDRC(encoding=3, text=metadata['date'])

        # Salva as alterações
        audio.save()

        logging.getLogger().debug(f"Metadados ID3 adicionados: {metadata}")

    except Exception as e:
        logging.getLogger().warning(f"Não foi possível adicionar metadados ID3: {e}")


def generate_audio_edge(text, output_path, metadata=None):
    """
    Backend: Microsoft Edge TTS (online, gratuito).

    Usa o serviço de TTS do Microsoft Edge.
    Não requer API key e tem vozes naturais em PT-BR.
    """
    import asyncio
    import edge_tts

    logger = logging.getLogger()

    # Voz em PT-BR - Thalita é a mais natural
    voice = "pt-BR-ThalitaMultilingualNeural"

    # Se quiser voz masculina, use: pt-BR-AntonioNeural
    # voice = "pt-BR-AntonioNeural"

    mp3_path = output_path.with_suffix('.mp3')

    try:
        async def _generate():
            communicate = edge_tts.Communicate(text, voice)
            await communicate.save(str(mp3_path))

        # Executa a coroutine
        asyncio.run(_generate())

        logger.debug(f"Áudio gerado: {mp3_path}")

        # Adicionar metadados ID3 se disponível
        if HAS_MUTAGEN and metadata:
            add_id3_metadata(mp3_path, metadata)

        return mp3_path

    except Exception as e:
        logger.error(f"Erro ao gerar áudio com Edge TTS: {e}")
        return None


def get_backend_function(backend_name):
    """
    Retorna a função do backend correspondente ao nome.

    Facilita adicionar novos backends sem modificar o código principal.
    """
    backends = {
        'say': generate_audio_say,
        'edge': generate_audio_edge,
        # Exemplos futuros:
        # 'fish': generate_audio_fish,
        # 'openai': generate_audio_openai,
        # 'elevenlabs': generate_audio_elevenlabs,
    }

    return backends.get(backend_name, generate_audio_say)


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


def process_article(md_file, force=False, dry_run=False, backend='say'):
    """
    Processa um arquivo markdown e gera o áudio.

    Args:
        md_file: Path do arquivo markdown
        force: Se True, regenera o áudio mesmo se já existir
        dry_run: Se True, só simula o processo sem gerar arquivos
        backend: Nome do backend TTS a usar

    Returns:
        Path do arquivo gerado ou None
    """
    logger = logging.getLogger()
    slug = get_article_slug(md_file)

    if not slug:
        logger.error(f"Não foi possível extrair slug de: {md_file}")
        return None

    # Extrair metadados do frontmatter para ID3
    metadata = extract_frontmatter(md_file)

    # Verificar se o áudio já existe
    audio_path = AUDIO_DIR / f"{slug}.mp3"

    if audio_path.exists() and not force:
        audio_mtime = audio_path.stat().st_mtime
        md_mtime = md_file.stat().st_mtime

        if audio_mtime > md_mtime:
            logger.info(f"✓ Áudio já existe e está atualizado: {audio_path.name}")
            return audio_path
        else:
            logger.debug(f"Markdown modificado desde a última geração: {slug}")

    logger.info(f"Processando: {slug}")

    # Extrair texto
    text = extract_text_from_markdown(md_file)

    if not text or len(text.strip()) < 100:
        logger.warning(f"Texto muito curto ou vazio: {slug}")
        return None

    # Limitar tamanho do texto (primeiros 5000 caracteres)
    text = text[:5000]

    if dry_run:
        logger.info(f"[DRY-RUN] Geraria áudio para: {slug} ({len(text)} caracteres)")
        return audio_path

    logger.debug(f"Gerando áudio para: {slug} ({len(text)} caracteres)")

    # Seleciona o backend
    backend_func = get_backend_function(backend)
    temp_aiff = AUDIO_DIR / f"{slug}.aiff"
    result = backend_func(text, temp_aiff, metadata)

    if result:
        logger.info(f"✓ Áudio gerado: {result.name}")
        return result
    else:
        logger.error(f"✗ Falha ao gerar áudio para: {slug}")
        return None


def main():
    """Função principal com argumentos de linha de comando."""
    # Configura parser de argumentos
    parser = argparse.ArgumentParser(
        description='Gera áudio dos artigos do blog usando TTS.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  %(prog)s                          # Processa todos os artigos (padrão: edge)
  %(prog)s --slug meu-post          # Processa apenas 'meu-post'
  %(prog)s --force                  # Força regeneração de todos
  %(prog)s --limit 5                # Processa apenas 5 artigos
  %(prog)s --dry-run                # Simula sem gerar arquivos
  %(prog)s --verbose                # Mostra logs detalhados
  %(prog)s --backend edge           # Usa backend Edge TTS (voz natural, padrão)
  %(prog)s --backend say            # Usa backend say (voz do macOS)
        """
    )

    parser.add_argument(
        '--slug',
        type=str,
        help='Processa apenas um artigo específico (pelo slug)'
    )

    parser.add_argument(
        '--force',
        action='store_true',
        help='Força regeneração do áudio mesmo se já existir'
    )

    parser.add_argument(
        '--limit',
        type=int,
        help='Limita o número de artigos a processar'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Simula o processo sem gerar arquivos'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Mostra logs detalhados (DEBUG)'
    )

    parser.add_argument(
        '--backend',
        type=str,
        default='edge',
        choices=['say', 'edge'],
        help='Backend TTS a usar (padrão: edge, opções: say, edge)'
    )

    args = parser.parse_args()

    # Configura logging
    logger = setup_logging(args.verbose)

    # Criar diretório de áudio se não existir
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)

    # Encontrar artigos
    if args.slug:
        # Busca artigo específico
        md_file = None
        for pattern in [f"**/{args.slug}/index.md", f"**/{args.slug}.md"]:
            matches = list(CONTENT_DIR.glob(pattern))
            if matches:
                md_file = matches[0]
                break

        if not md_file or not md_file.exists():
            logger.error(f"Artigo não encontrado: {args.slug}")
            sys.exit(1)

        articles = [md_file]
        logger.info(f"Processando artigo específico: {args.slug}")
    else:
        # Busca todos os artigos
        articles = list(CONTENT_DIR.glob(BLOG_PATTERN))
        articles.sort(key=lambda p: p.stat().st_mtime, reverse=True)  # Mais recentes primeiro

    # Aplica limite se especificado
    if args.limit:
        articles = articles[:args.limit]
        logger.info(f"Limitando a {args.limit} artigos")

    logger.info(f"Encontrados {len(articles)} artigos")
    logger.info(f"Diretório de áudio: {AUDIO_DIR}")
    logger.info(f"Backend TTS: {args.backend}")

    if args.dry_run:
        logger.info("[MODO DRY-RUN] Nenhum arquivo será gerado")

    logger.info("-" * 60)

    # Processa cada artigo
    processed = 0
    failed = 0
    skipped = 0

    # Usa tqdm para barra de progresso se disponível e não estiver em verbose
    use_tqdm = HAS_TQDM and not args.verbose and not args.dry_run and len(articles) > 1

    if use_tqdm:
        iterator = tqdm(articles, desc="Gerando áudios", unit="artigo")
    else:
        iterator = enumerate(articles, 1)

    for item in iterator:
        if use_tqdm:
            md_file = item
            logger.debug(f"Processando: {md_file}")
        else:
            i, md_file = item
            if not args.verbose:
                print(f"\n[{i}/{len(articles)}]", end=" ")

        result = process_article(
            md_file,
            force=args.force,
            dry_run=args.dry_run,
            backend=args.backend
        )

        if result:
            if result.exists():
                processed += 1
            else:
                skipped += 1
        else:
            failed += 1

    # Resumo
    logger.info("=" * 60)
    logger.info("Processamento concluído!")
    logger.info(f"Gerados: {processed}")
    logger.info(f"Ignorados (já existem): {skipped}")
    logger.info(f"Falhas: {failed}")
    logger.info(f"Total: {len(articles)}")

    # Retorna código de erro se houver falhas
    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
