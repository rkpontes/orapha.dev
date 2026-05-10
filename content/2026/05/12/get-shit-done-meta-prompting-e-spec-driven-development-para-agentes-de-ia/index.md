---
title: "Get Shit Done: Meta-prompting e spec-driven development que realmente funciona"
date: '2026-05-12T10:00:00-03:00'
slug: get-shit-done-meta-prompting-e-spec-driven-development-para-agentes-de-ia
translationKey: get-shit-done-meta-prompting-e-spec-driven-development-para-agentes-de-ia-2026-05-12
tags:
  - ia
  - spec-driven-development
  - claude-code
  - meta-prompting
  - context-engineering
draft: false
description: "Um sistema leve e poderoso de meta-prompting e spec-driven development para Claude Code, OpenCode, Gemini CLI e outros. Resolve o context rot que degrada a qualidade das sessões longas com IA."
---

# Get Shit Done: Meta-prompting e spec-driven development que realmente funciona

Sessões longas com agentes de IA têm um problema silencioso: **context rot**. Quanto mais você usa o agente, mais a qualidade degrada. O contexto vai enchendo, o agente começa a esquecer coisas que vocês discutiram no início, as respostas ficam mais genéricas, os erros mais frequentes.

Eu já passei por isso. Você começa uma sessão animado, o agente entrega código excelente nas primeiras horas, mas depois de umas 10-15 interações, a coisa desanda. Ele sugere soluções que contradizem o que vocês combinaram, propõe refatorações desnecessárias, ou simplesmente perde o rumo do que você queria construir.

O problema não é o modelo. É como a gente gerencia o contexto.

Foi aí que eu descobri o [**Get Shit Done (GSD)**](https://github.com/gsd-build/get-shit-done).

## O que é GSD?

É um sistema leve de meta-prompting, context engineering e spec-driven development criado por TÂCHES. A proposta é simples: resolver o context rot mantendo seu contexto principal limpo, fazendo o trabalho pesado em subagents com contextos novos.

A diferença para outras ferramentas de spec-driven development? GSD foi feito para desenvolvedores que trabalham sozinhos, não para organizações de 50 pessoas com cerimônias de sprint e fluxos do Jira. A complexidade está no sistema, não no seu workflow.

## O loop de 6 comandos

O GSD opera em um loop simples de seis comandos:

### 1. Initialize
```
/gsd-new-project
```
Perguntas → pesquisa → requisitos → roadmap. Você aprova, aí começa a construção.

Já tem código? Rode `/gsd-map-codebase` primeiro. Ele analisa seu stack, arquitetura e convenções para que o novo projeto faça as perguntas certas.

### 2. Discuss
```
/gsd-discuss-phase 1
```
Seu roadmap tem uma frase por fase. Isso não é suficiente para construir do jeito que *você* imagina. O discuss captura suas decisões antes do planejamento: layouts, estrutura da API, tratamento de erros, data structures — qualquer área cinzenta dessa fase específica.

Pula essa etapa, você recebe padrões razoáveis. Usa ela, você recebe sua visão.

### 3. Plan
```
/gsd-plan-phase 1
```
Pesquisa → planejamento → verificação, em loop até os planos passarem. Cada plano é pequeno o suficiente para executar em uma janela de contexto nova.

### 4. Execute
```
/gsd-execute-phase 1
```
Planos executam em batches paralelos. Cada executor recebe 200k tokens de contexto novo. Cada task recebe seu próprio commit atômico. Você sai, volta, e encontra o trabalho completo com um histórico git limpo.

Sua janela de contexto principal fica em 30-40%. O trabalho acontece nos subagents.

> PHASE é como você divide o trabalho dentro de uma milestone.

### 5. Verify
```
/gsd-verify-work 1
```
Você revisa o que foi construído. Qualquer coisa quebrada recebe um plano de correção diagnosticado — pronto para nova execução imediata. Você não debuga manualmente; só roda execute de novo.

### 6. Repeat → Ship
```
/gsd-ship 1
/gsd-complete-milestone
/gsd-new-milestone
```

Loop discuss → plan → execute → verify → ship até a milestone terminar. Depois arquiva, cria tag, e começa a próxima do zero.

> SHIP é o comando que cria o Pull Request com o trabalho verificado da fase.

> Milestones são agrupamentos de fases que fazem sentido juntas. Você define quantas fases quer em cada milestone.

## Por que funciona

Três coisas que a maioria dos setups de AI-coding erra:

**1. Acúmulo de contexto.** Quanto mais a sessão cresce, mais a qualidade degrada. GSD mantém seu contexto principal limpo fazendo o trabalho pesado em contextos novos de subagents. Pesquisadores, planejadores e executores cada um começam do zero com exatamente o que precisam.

**2. Sem memória compartilhada.** GSD mantém artefatos estruturados que sobrevivem entre sessões:
- `PROJECT.md` — visão
- `REQUIREMENTS.md` — escopo
- `ROADMAP.md` — para onde você vai
- `STATE.md` — posição atual e decisões
- `CONTEXT.md` — decisões de implementação por fase

Toda nova sessão carrega esses arquivos e sabe exatamente onde as coisas estão.

**3. Sem verificação.** Código que "roda" não é código que "funciona." O passo de verify do GSD te guia pelo que foi construído, diagnostica falhas com agents de debug dedicados, e gera planos de correção antes de você declarar uma fase completa.

## Instalação

A instalação é simples:

```bash
npx get-shit-done-cc@latest
```

O instalador pergunta seu runtime (Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf, e mais) e se quer instalar global ou localmente.

```bash
claude --dangerously-skip-permissions
opencode --dangerously-skip-permissions
gemini-cli --dangerously-skip-permissions
# ... dependendo do seu agente
```

GSD é feito para automação sem fricção. Skip-permissions é o modo recomendado para rodar.

## Comandos principais

| Comando | O que faz |
|---------|-----------|
| `/gsd-new-project` | Perguntas → pesquisa → requisitos → roadmap |
| `/gsd-discuss-phase [N]` | Captura decisões de implementação antes do planejamento |
| `/gsd-plan-phase [N]` | Pesquisa + planejamento + verificação |
| `/gsd-execute-phase <N>` | Executa planos em batches paralelos |
| `/gsd-verify-work [N]` | Testes de aceitação manuais |
| `/gsd-ship [N]` | Cria PR do trabalho verificado da fase |
| `/gsd-progress --next` | Auto-detecta e roda o próximo passo |
| `/gsd-complete-milestone` | Arquiva milestone e cria tag de release |
| `/gsd-new-milestone` | Começa próxima versão |

## Configuração

As configurações ficam em `.planning/config.json`. Algumas opções chave:

| Config | O que controla |
|--------|----------------|
| `mode` | `interactive` (confirma cada passo) ou `yolo` (auto-aprova) |
| Model profiles | `quality` / `balanced` / `budget` — controla qual modelo cada agente usa |
| `workflow.research` / `plan_check` / `verifier` | Liga/desliga agents de qualidade que adicionam tokens e tempo |
| `parallelization.enabled` | Roda planos independentes simultaneamente |

## O que me conquistou

O GSD tem 61k+ estrelas no GitHub e é usado por engenheiros da Amazon, Google, Shopify e Webflow. O que me conquistou foi a simplicidade: são poucos comandos que fazem exatamente o que prometem.

Não é over-engineered. Não tenta ser uma plataforma enterprise. É um sistema que entende que devs que trabalham sozinhos precisam de algo que funcione sem burocracia.

A ideia de manter artefatos estruturados que sobrevivem entre sessões é genial. Você pode fechar o laptop, voltar amanhã, e o agente sabe exatamente onde parou. Não precisa re-explicar nada.

E o verify step é algo que eu não via em outras ferramentas. A maioria para no "execute" e assume que funcionou. GSD te obriga a verificar, e quando encontra problemas, já gera o plano de correção.

## Considerações

Se você usa Claude Code (ou outro agente) regularmente e sente que a qualidade degrada em sessões longas, GSD é praticamente obrigatório. É a diferença entre "o agente às vezes funciona" e "o agente é confiável".

A curva de aprendizado é suave — são seis comandos principais — mas o impacto na qualidade do código entregue é imenso.

---

**Links:**
- [Get Shit Done no GitHub](https://github.com/gsd-build/get-shit-done)
- [Documentação completa](https://github.com/gsd-build/get-shit-done/blob/main/docs/USER-GUIDE.md)
- [Arquitetura](https://github.com/gsd-build/get-shit-done/blob/main/docs/ARCHITECTURE.md)
- [Discord da comunidade](https://discord.gg/mYgfVNfA2r)
