# Sistema de Text-to-Speech (TTS) para o Blog

Este diretório contém scripts para gerar áudio dos artigos do blog usando TTS (Text-to-Speech) 100% offline.

## 📁 Estrutura

```
scripts/
├── generate_audio.py    # Script principal para gerar áudios
├── README.md           # Este arquivo
└── requirements.txt    # Dependências Python (opcional)

static/audio/           # Áudios gerados (MP3)
```

## 🎯 Funcionamento

### Backend Atual: macOS `say` (Nativo)

O script atual utiliza o comando `say` nativo do macOS, que é:
- ✅ 100% offline
- ✅ Rápido
- ✅ Não requer instalação de modelos pesados
- ✅ Usa a voz "Luciana" (PT-BR) quando disponível

### Backend Futuro: Fish Speech

Para usar o Fish Speech (qualidade superior), você precisará:

1. Instalar as dependências:
```bash
source .venv/bin/activate
pip install fish-speech transformers huggingface-hub
```

2. Modificar o script `generate_audio.py` para usar o Fish Speech em vez do `say`

## 🚀 Como Usar

### Gerar áudio para TODOS os artigos:

```bash
# Ativar ambiente virtual
source .venv/bin/activate

# Gerar todos os áudios
python3 scripts/generate_audio.py
```

### Gerar áudio para um artigo específico:

```bash
# Edite o script e descomente a seção no final:
# article = Path("content/2026/05/09/nome-do-artigo/index.md")
# process_article(article)
```

### Adicionar áudio a um novo artigo:

1. Escreva o artigo em `content/ANO/MES/DIA/slug-do-artigo/index.md`
2. Execute o script para gerar o áudio
3. O player aparecerá automaticamente no artigo

## 🎵 Player de Áudio

O player está integrado automaticamente em todos os artigos que têm áudio gerado. Ele aparece:
- ✅ Abaixo do título e data
- ✅ Acima do conteúdo do artigo
- ✅ Com controles de play/pause
- ✅ Com barra de progresso
- ✅ Com tempo atual/duração

### Como funciona no Hugo:

O template `layouts/single.html` verifica se existe um arquivo de áudio correspondente:
- Se existir: mostra o player funcional
- Se não existir: oculta o player automaticamente

## ⚙️ Configurações

### Limitar tamanho do texto

Por padrão, o script processa apenas os primeiros 5000 caracteres de cada artigo para evitar áudios muito longos. Para alterar:

```python
# No arquivo generate_audio.py, linha ~150
text = text[:5000]  # Altere este valor
```

### Qualidade do áudio

A qualidade do MP3 é configurada no ffmpeg (linha 58):
```python
'-qscale:a', '2',  # 0 = melhor qualidade, 9 = menor qualidade
```

## 🔄 Atualização de Áudios

O script é inteligente e só regenera áudios quando necessário:
- Se o arquivo MP3 já existe e é mais recente que o markdown → não regenera
- Se o markdown foi modificado → regenera automaticamente

## 🛠️ Solução de Problemas

### Erro: "ffmpeg not found"
Instale o ffmpeg:
```bash
brew install ffmpeg
```

### Erro: "say command not found"
Você não está no macOS. Use uma alternativa como Coqui TTS ou Edge-TTS.

### Áudio não aparece no site
1. Verifique se o arquivo MP3 existe em `static/audio/`
2. Verifique se o nome do slug no markdown corresponde ao nome do arquivo
3. Faça um rebuild do Hugo: `hugo --gc`

### Voz em inglês em vez de português
A voz "Luciana" (PT-BR) pode não estar instalada. Para instalar:
1. Vá em Configurações do Sistema → Acessibilidade → Fala
2. Clique em "Gerenciar vozes..."
3. Procure por "Luciana" e instale

## 📝 Notas

- Os áudios são gerados em formato MP3 para compatibilidade máxima
- O tamanho médio dos arquivos é de 2-3MB por artigo
- O tempo de geração é de aproximadamente 10-20 segundos por artigo
- Recomenda-se gerar os áudios em lotes para não sobrecarregar o sistema

## 🔮 Futuras Melhorias

- [ ] Integrar Fish Speech para qualidade superior
- [ ] Suporte a múltiplas vozes
- [ ] Opção de gerar áudio apenas para artigos novos
- [ ] Webhook para geração automática no CI/CD
- [ ] Cache de áudios no CDN
