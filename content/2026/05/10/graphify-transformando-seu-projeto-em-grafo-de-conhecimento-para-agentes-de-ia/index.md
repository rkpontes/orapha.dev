---
title: "Graphify: Transformando seu projeto em um grafo de conhecimento que agentes de IA entendem"
date: '2026-05-10T10:00:00-03:00'
slug: graphify-transformando-seu-projeto-em-grafo-de-conhecimento-para-agentes-de-ia
translationKey: graphify-transformando-seu-projeto-em-grafo-de-conhecimento-para-agentes-de-ia-2026-05-10
tags:
  - ia
  - knowledge-graph
  - graphify
  - claude-code
  - codex
  - opencode
draft: false
description: "Como transformar qualquer pasta de código, documentos, PDFs e até vídeos em um grafo de conhecimento consultável. Uma skill para Claude Code, Codex, OpenCode e outros agentes de IA."
---

# Graphify: Transformando seu projeto em um grafo de conhecimento que agentes de IA entendem

Trabalhar com projetos grandes usando agentes de IA tem um problema clássico: o contexto. Você abre o chat, faz uma pergunta sobre como a autenticação funciona no seu sistema, e o agente começa a grep-ar por aí, abrindo arquivos aleatórios, perdendo tempo com código irrelevante. Quando seu projeto tem milhares de arquivos, essa abordagem de "procurar no escuro" não escala.

Eu passei por isso várias vezes. E a verdade é que os agentes são bons em entender código, mas ruins em entender a **estrutura** do código. Eles não têm um mapa mental do projeto. Não sabem o que está conectado com o quê, não enxergam os padrões arquiteturais, não captam as decisões de design que estão espalhadas em comentários e documentação.

Foi aí que eu descobri o [**Graphify**](https://github.com/safishamsi/graphify).

## O que é Graphify?

Graphify é uma skill para agentes de código (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, e mais) que transforma qualquer pasta de conteúdo em um **grafo de conhecimento consultável**.

E quando digo "qualquer pasta", estou falando de:
- Código em 28 linguagens (Python, TypeScript, Go, Rust, Java, etc.)
- SQL schemas
- Scripts shell
- Documentação (Markdown, HTML, TXT)
- Arquivos Office (docx, xlsx)
- PDFs
- Imagens (PNG, JPG, WebP)
- Vídeos e áudio (MP4, MOV, MP3, WAV)
- URLs do YouTube
- Documentos do Google Workspace

A ideia é simples: em vez de deixar o agente garimpando arquivos no escuro, você cria um mapa inteligente do projeto que ele pode navegar.

## Como funciona

A instalação é direta:

```bash
uv tool install graphifyy && graphify install
# ou: pipx install graphifyy && graphify install
# ou: pip install graphifyy && graphify install
```

Depois, é só rodar no seu projeto:

```
/graphify .
```

Pronto. Graphify vai gerar três arquivos:

```
graphify-out/
├── graph.html       # Visualização interativa — abre no navegador
├── GRAPH_REPORT.md  # Resumo executivo com destaques e perguntas sugeridas
└── graph.json       # Grafo completo para consulta programática
```

O `graph.html` é particularmente útil. Você pode clicar nos nós, filtrar, pesquisar. É uma forma visual de entender como as peças do seu projeto se conectam.

## O que tem no relatório

O `GRAPH_REPORT.md` é onde a coisa fica interessante. Ele inclui:

- **God nodes** — os conceitos mais conectados do projeto. Tudo passa por eles.
- **Conexões surpreendentes** — links entre coisas que vivem em arquivos ou módulos diferentes, ranqueadas por quão inesperadas são.
- **O "porquê"** — comentários inline (`# NOTE:`, `# WHY:`, `# HACK:`) e docstrings extraídos como nós separados.
- **Perguntas sugeridas** — 4-5 perguntas que o grafo está posicionado para responder.
- **Tags de confiança** — cada relação é marcada como `EXTRACTED` (achado no código), `INFERRED` (inferido) ou `AMBIGUOUS` (ambíguo).

Isso significa que você pode perguntar ao agente: "o que conecta autenticação ao banco de dados?" e ele vai consultar o grafo em vez de ficar grep-ando.

## Integração com agentes

O Graphify tem integração nativa com várias plataformas:

| Plataforma | Comando |
|------------|---------|
| Claude Code | `graphify install` |
| Codex | `graphify install --platform codex` |
| OpenCode | `graphify install --platform opencode` |
| Cursor | `graphify cursor install` |
| VS Code Copilot Chat | `graphify vscode install` |
| GitHub Copilot CLI | `graphify install --platform copilot` |
| Gemini CLI | `graphify install --platform gemini` |
| Aider | `graphify install --platform aider` |

Depois de instalar, você pode fazer com que o agente sempre use o grafo:

```bash
graphify claude install
```

Isso escreve um arquivo de configuração que diz ao assistente para ler o `GRAPH_REPORT.md` antes de responder perguntas sobre seu codebase. Em plataformas que suportam hooks (Claude Code, Codex, Gemini CLI), um hook dispara automaticamente antes de cada chamada de leitura de arquivo.

## Consultando o grafo

Além de deixar o agente usar automaticamente, você pode consultar o grafo diretamente:

```
/graphify query "what connects auth to the database?"
/graphify path "UserService" "DatabasePool"
/graphify explain "RateLimiter"
```

Ou via terminal:

```bash
graphify query "show the auth flow"
graphify query "what connects DigestAuth to Response?" --graph graphify-out/graph.json
```

Para integração com MCP (Model Context Protocol), você pode expor o grafo como servidor:

```bash
python -m graphify.serve graphify-out/graph.json
```

Isso dá ao seu assistente acesso estruturado via funções como `query_graph`, `get_node`, `get_neighbors`, `shortest_path`.

## Time e versionamento

O Graphify foi pensado para trabalho em equipe. O diretório `graphify-out/` foi feito para ser commitado no git. O workflow recomendado:

1. Uma pessoa roda `/graphify .` e comita o `graphify-out/`
2. Todo mundo dá pull — seus assistentes já leem o grafo imediatamente
3. Roda `graphify hook install` para auto-rebuild a cada commit
4. Quando docs ou papers mudam, roda `/graphify --update`

Tem até um merge driver para evitar conflitos em `graph.json` quando dois devs commitam em paralelo.

## Privacidade

Uma coisa que me importa é privacidade. Aqui está como funciona:

- **Arquivos de código** — processados localmente via tree-sitter. Nada sai da sua máquina.
- **Vídeo/áudio** — transcrito localmente com faster-whisper. Nada sai da sua máquina.
- **Docs, PDFs, imagens** — enviados para seu assistente de IA para extração semântica (usando o modelo da sua sessão IDE).

Não tem telemetria, não tem tracking, não tem analytics.

## Por que isso importa

Para mim, o valor do Graphify está em três lugares:

**Primeiro, eficiência.** Em vez de deixar o agente abrindo dezenas de arquivos procurando contexto, ele navega por um grafo estruturado. Menos tokens gastos, respostas mais rápidas.

**Segundo, descoberta.** O grafo mostra conexões que você talvez não percebesse. Aquela função utilitária que é usada em 15 lugares diferentes. Aquele módulo que é ponte entre dois domínios aparentemente desconectados.

**Terceiro, onboarding.** Quando alguém novo entra no projeto, o grafo é um mapa. Em vez de ler milhares de arquivos, você explora o grafo. Vê os god nodes, entende a arquitetura, descobre os padrões.

## Considerações finais

O Graphify é uma daquelas ferramentas que parece óbvia depois que você usa. Transformar código em grafo de conhecimento faz total sentido quando você trabalha com agentes de IA. É como dar a eles um mapa em vez de deixar eles explorando no escuro.

Se você trabalha com projetos grandes e usa agentes de código regularmente, vale a pena experimentar. A curva de aprendizado é praticamente zero — instala, roda `/graphify .`, e começa a usar.

O repositório tem 45k+ estrelas e uma comunidade ativa. Está em constante evolução com suporte para novas plataformas e formatos de arquivo.

---

**Links:**
- [Graphify no GitHub](https://github.com/safishamsi/graphify)
- [Documentação completa](https://github.com/safishamsi/graphify/blob/v7/docs/how-it-works.md)
- [Site oficial](https://graphifylabs.ai)
