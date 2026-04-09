---
title: "OpenSpec na prática: instalação, uso, fluxo completo e comandos opcionais"
date: '2026-04-08T10:00:00-03:00'
slug: openspec-na-pratica-instalacao-uso-fluxo-completo-e-comandos-opcionais
tags:
  - ia
  - openspec
  - spec-driven-development
  - engenharia-de-software
  - desenvolvimento
draft: false
description: "Um guia completo e direto para instalar e usar o OpenSpec no dia a dia: pré-requisitos, estrutura, fluxo recomendado e comandos opcionais que valem conhecer."
---

# OpenSpec na prática: instalação, uso, fluxo completo e comandos opcionais

Se você já usa agente de código no dia a dia, já percebeu o padrão: quando a intenção está vaga, a saída também fica vaga. Foi por isso que comecei a estudar com mais atenção ferramentas de **Spec-Driven Development (SDD)** e, nessa jornada, o **OpenSpec** virou uma opção bem interessante.

A proposta dele é simples: antes de sair implementando, você organiza a mudança em artefatos claros (proposta, specs, tarefas e, quando necessário, design), executa com mais previsibilidade e mantém histórico do que mudou no comportamento esperado do sistema.

Neste artigo, vou detalhar tudo que você pediu, de forma prática:

1. Como instalar o OpenSpec.
2. Como iniciar em um projeto novo ou existente.
3. Qual flow eu recomendo no uso diário.
4. Quais comandos opcionais vale conhecer (CLI e slash commands).

## O que é o OpenSpec (sem enrolação)

O OpenSpec é um framework open source de SDD para trabalho com assistentes de IA. Ele adiciona uma camada de especificação no repositório para reduzir improviso e aumentar previsibilidade.

A estrutura principal fica dentro de `openspec/`:

- `openspec/specs/`: fonte de verdade atual do sistema.
- `openspec/changes/`: mudanças propostas em andamento.
- `openspec/changes/archive/`: mudanças já concluídas e arquivadas.

O valor real está nessa separação: você consegue enxergar claramente o estado atual e o que está sendo proposto, sem misturar tudo em conversa de chat.

## Pré-requisitos

Antes de instalar, garanta:

- `Node.js >= 20.19.0`
- Um gerenciador de pacotes (`npm`, `pnpm`, `yarn` ou `bun`)
- Um projeto local (pode ser brownfield, sem problema)
- Um agente de código compatível (Codex, Claude Code, Cursor, Copilot etc.)

Comandos rápidos para validar ambiente:

```bash
node --version
npm --version
```

## Instalação do OpenSpec CLI

### Com npm

```bash
npm install -g @fission-ai/openspec@latest
```

### Com pnpm

```bash
pnpm install -g @fission-ai/openspec@latest
```

### Com yarn

```bash
yarn global add @fission-ai/openspec@latest
```

### Com bun

```bash
bun install -g @fission-ai/openspec@latest
```

Depois da instalação:

```bash
openspec --version
```

Se esse comando retornar a versão, a CLI está pronta.

## Inicializando no projeto

No diretório raiz do projeto:

```bash
cd meu-projeto
openspec init
```

Na prática, esse comando:

- cria a pasta `openspec/`
- gera instruções para o agente (incluindo `AGENTS.md` no projeto)
- configura integrações para ferramentas suportadas

Depois do `init`, eu gosto de rodar:

```bash
openspec list
```

Isso já confirma se a estrutura está ativa e se há mudanças abertas.

## Estrutura gerada e como ler isso

Um fluxo típico de mudança fica assim:

```text
openspec/
├── specs/
│   └── auth/
│       └── spec.md
└── changes/
    └── add-2fa/
        ├── proposal.md
        ├── tasks.md
        ├── design.md (opcional)
        └── specs/
            └── auth/
                └── spec.md
```

Interpretação prática:

- `proposal.md`: por que mudar e o que vai mudar.
- `specs/*`: deltas de requisito/comportamento.
- `tasks.md`: checklist de implementação.
- `design.md`: decisões técnicas quando necessário.

## Flow recomendado para usar OpenSpec no dia a dia

Esse é o fluxo que considero mais equilibrado entre rigor e velocidade.

### 1) Criar proposta da mudança

No agente, peça uma proposta OpenSpec para uma feature específica.

Exemplo com shortcut (quando a ferramenta suporta):

```text
/openspec:proposal Add profile search filters
```

### 2) Revisar e validar antes de implementar

No terminal:

```bash
openspec list
openspec validate add-profile-search-filters
openspec show add-profile-search-filters
```

Aqui é onde você corta ambiguidade e evita retrabalho.

### 3) Refinar proposal/specs/tasks

Se faltar clareza, peça para o agente ajustar critérios, cenários e tarefas até ficar executável.

### 4) Implementar com base nas tarefas

```text
/openspec:apply add-profile-search-filters
```

A ideia é implementar em cima do `tasks.md` e não no improviso.

### 5) Arquivar a mudança concluída

No agente:

```text
/openspec:archive add-profile-search-filters
```

Ou via CLI:

```bash
openspec archive add-profile-search-filters --yes
```

Quando você arquiva, a mudança sai do estado “em andamento” e passa a compor o histórico consolidado.

## Comandos principais (CLI)

No uso real, estes são os comandos que mais importam:

```bash
openspec init
openspec list
openspec view
openspec show <change>
openspec validate <change>
openspec archive <change> --yes
openspec update
```

Resumo rápido:

- `init`: inicializa OpenSpec no repo.
- `list`: lista mudanças abertas.
- `view`: dashboard interativo.
- `show`: exibe proposal/tasks/spec deltas de uma mudança.
- `validate`: valida formato/estrutura das specs.
- `archive`: arquiva mudança concluída.
- `update`: atualiza instruções e bindings para agentes no projeto.

## Comandos de atalho no agente

Dependem da ferramenta, mas o padrão atual do OpenSpec em várias integrações nativas é:

- `/openspec:proposal`
- `/openspec:apply`
- `/openspec:archive`

Em alguns contextos/documentações você também vai encontrar o fluxo **OPSX** (experimental), com comandos como:

- `/opsx:new`
- `/opsx:continue`
- `/opsx:ff`
- `/opsx:apply`
- `/opsx:archive`

O ponto importante: confira qual conjunto de comandos sua integração instalou no `init`.

## Erros comuns (e como evitar)

1. Pular revisão da proposta e ir direto para implementação.
2. Aceitar `tasks.md` sem conferir ordem e dependências.
3. Não validar specs (`validate`) antes de aplicar.
4. Misturar comandos de docs diferentes sem checar sua integração.
5. Não arquivar mudança concluída (vira bagunça rápido).

## Um exemplo de execução ponta a ponta

```bash
# 1) Instalar
npm install -g @fission-ai/openspec@latest

# 2) Inicializar no projeto
cd meu-projeto
openspec init

# 3) Conferir estado
openspec list

# 4) No agente, criar proposta
# /openspec:proposal Add profile search filters

# 5) Revisar no terminal
openspec validate add-profile-search-filters
openspec show add-profile-search-filters

# 6) No agente, implementar
# /openspec:apply add-profile-search-filters

# 7) Arquivar mudança
openspec archive add-profile-search-filters --yes
```

## Fechando

Quando você instala, inicializa e segue um flow mínimo de proposta, revisão, aplicação e arquivo, a qualidade da execução com agente sobe muito.

E o melhor: você mantém rastreabilidade real da intenção técnica, sem depender de memória de chat.
