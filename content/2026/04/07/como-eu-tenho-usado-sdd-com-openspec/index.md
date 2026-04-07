---
title: "Como eu tenho usado Spec-Driven Development com OpenSpec"
date: '2026-04-07T10:00:00-03:00'
slug: como-eu-tenho-usado-sdd-com-openspec
tags:
  - ia
  - spec-driven-development
  - openspec
  - engenharia-de-software
  - desenvolvimento
draft: false
description: "Como usar OpenSpec para estruturar desenvolvimento com IA sem cair em burocracia ou prompt solto."
---

# Como eu tenho usado Spec-Driven Development com OpenSpec

Se você tá usando IA pra programar de verdade, e não só pra fazer protótipo, uma hora você percebe uma coisa:

quanto mais importante o projeto, mais perigoso é ficar se guiando por prompt solto.

No começo até funciona. Você pede uma coisa, ajusta ali, muda outra aqui e vai levando.

Mas depois começa a degringolar.

O agente decide coisa que você não pediu, a arquitetura vai ficando meio torta, você passa mais tempo refatorando do que construindo… e qualquer mudança vira uma mini negociação.

E foi aqui que a ficha caiu pra mim:

**o problema não é a IA.
é a falta de estrutura entre intenção e código.**

---

## Quando o Spec Kit começou a pesar

Por um tempo, eu tentei resolver isso com Spec-Driven Development usando Spec Kit.

Inclusive tem um artigo aqui no blog sobre isso:

* [No Spec-Driven Development, tudo começa pelos princípios](/2026/04/03/como-eu-tenho-usado-spec-driven-development-com-o-spec-kit-nos-meus-projetos)

A ideia é boa. Funciona.

Mas no uso real… começou a incomodar.

Principalmente por um motivo:

👉 **tokens**

Cada etapa gerava muito conteúdo, muito detalhamento, muito overhead.

E dependendo do fluxo, os tokens iam embora ligeiro demais, parecia água escorrendo.

Pra times grandes, talvez isso faça sentido.

Mas no meu dia a dia, começou a ficar pesado demais.

---

## Por que eu fui testar o OpenSpec

Foi aí que eu comecei a testar o OpenSpec.

O que me chamou atenção nele foi justamente o oposto:

* mais leve
* mais direto
* menos verboso

A proposta é simples:

manter a estrutura do Spec-Driven Development
sem transformar isso num processo pesado

E isso, pra mim, fez muito mais sentido.

---

## O OpenSpec na prática (instalação + uso)

Antes de tudo, você instala:

```bash
npm install -g @fission-ai/openspec@latest
```

Depois, no seu projeto:

```bash
openspec init
```

Isso já prepara o ambiente.

Ele cria a estrutura:

* `openspec/specs` → fonte de verdade do sistema
* `openspec/changes` → mudanças em andamento

Depois disso, você praticamente para de usar CLI.

Você passa a usar comandos dentro do agente (Claude Code, Codex, etc).

---

## O fluxo básico (o que você realmente usa)

No dia a dia, você só precisa disso aqui:

```
/opsx:propose → /opsx:apply → /opsx:archive
```

Sem complicação.

E o mais interessante:

o OpenSpec não trabalha com “fases travadas”.

Ele trabalha com **ações**.

Você pode voltar, ajustar, refazer, sem ficar preso num fluxo rígido.

---

## Como eu uso no dia a dia

Quando vou começar uma mudança, faço assim:

```
/opsx:propose adicionar filtro de status na listagem de pedidos
```

A partir disso, ele gera:

* proposal (por que isso existe)
* specs (o que deve acontecer)
* design (como será feito)
* tasks (passo a passo)

Tudo dentro de uma change.

E isso aqui resolve um problema enorme:

👉 tirar a decisão da cabeça e tornar explícito

Porque enquanto tá na cabeça, cada um interpreta de um jeito.

Depois disso, eu reviso.

E só depois disso eu rodo:

```
/opsx:apply
```

Aí o agente executa as tasks.

Aqui muda completamente o jogo:

eu não tô mais pedindo código
eu tô executando um plano

Quando termina:

```
/opsx:archive
```

Isso consolida tudo e atualiza as specs do projeto.

Ou seja:

👉 o sistema aprende com o que você fez

---

## Onde a doc do OpenSpec entra de verdade

Uma coisa que eu gostei é que o OpenSpec não te força a usar tudo.

Mas se você quiser aprofundar, ele tem mais comandos:

* `/opsx:explore` → entender problema antes de implementar
* `/opsx:new` → criar change manualmente
* `/opsx:continue` → criar artefatos passo a passo
* `/opsx:ff` → gerar tudo de uma vez
* `/opsx:verify` → validar se implementação bate com spec

Mas aqui vai o ponto importante:

👉 você não precisa disso pra começar

---

## Quando usar cada coisa (sem frescura)

### Use o fluxo simples quando:

* já sabe o que quer fazer
* é feature direta
* quer velocidade

👉 `/opsx:propose → apply → archive`

---

### Use `/opsx:explore` quando:

* você não sabe o problema direito
* é performance, arquitetura, bug estranho

👉 evita sair codando no escuro

---

### `/opsx:ff` vs `/opsx:continue`

* `/opsx:ff` → rápido, cria tudo
* `/opsx:continue` → mais controle

Minha regra:

se sei o que quero → ff
se ainda tô pensando → continue

---

### `/opsx:verify` (subestimado)

Esse aqui é forte.

Ele verifica:

* se tudo foi implementado
* se bate com a spec
* se a arquitetura faz sentido

Não bloqueia.

Mas evita fechar coisa errada.

---

## O que muda na prática

Sem isso:

* cada dev interpreta do seu jeito
* decisões no improviso
* retrabalho constante

Com OpenSpec:

* intenção clara
* execução baseada em plano
* conhecimento registrado

Resultado:

* menos ambiguidade
* mais previsibilidade
* menos retrabalho

---

## Onde você precisa ter cuidado

Não é mágica.

Se a proposta for ruim → o resultado vai ser ruim.

Outra coisa:

pra quem vem de processo pesado, pode parecer simples demais.

Mas isso é escolha.

E claro:

ainda precisa revisar código.

Spec não substitui pensamento crítico.

---

## Fechando

OpenSpec não é sobre documentar.

É sobre alinhar.

Porque no fim:

IA não erra porque é burra
IA erra porque a gente não foi claro

E quando você melhora isso:

* o código melhora
* o processo melhora
* a frustração diminui

Pra mim, o ponto é esse.

Não parar de usar IA.

Mas parar de usar IA de qualquer jeito.
