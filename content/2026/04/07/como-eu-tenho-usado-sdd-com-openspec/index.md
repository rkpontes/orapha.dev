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

Mas depois começam a aparecer umas coisas chatas:

o agente decide coisa que você não pediu, a arquitetura vai ficando meio torta, você passa mais tempo refatorando do que construindo… e qualquer mudança vira uma mini negociação.

E foi aqui que a ficha caiu pra mim:

**o problema não é a IA.  
é a falta de estrutura entre intenção e código.**

Por um tempo, eu tentei resolver isso com Spec-Driven Development usando Spec Kit. Inclusive tem um artigo aqui no blog sobre isso.

- [No Spec-Driven Development, tudo começa pelos princípios](/2026/04/03/como-eu-tenho-usado-spec-driven-development-com-o-spec-kit-nos-meus-projetos)

A ideia faz sentido demais, e na prática ajuda mesmo a organizar o processo.

Só que tinha uma coisa que começou a me incomodar com o tempo: o volume de tokens.

Cada etapa gerava muito conteúdo, muito detalhamento, muito overhead. E dependendo do fluxo, os tokens iam embora ligeiro demais, parecia água escorrendo.

Pra alguns contextos isso pode até fazer sentido. Mas, no meu dia a dia, começou a pesar mais do que ajudar.

Foi aí que eu comecei a testar o OpenSpec.

O que me chamou atenção nele foi justamente o oposto: mais leve, mais direto, menos verboso.

Ainda tô explorando, mas a expectativa é simples:

manter a estrutura do SDD, sem ver os tokens se acabando no meio do caminho.

Não como mais um processo burocrático, mas como um jeito simples de parar de fazer tudo no improviso.

---

## O OpenSpec na prática

Antes de sair usando, você precisa instalar o OpenSpec no seu ambiente.

Ele é bem mais simples que outras ferramentas nesse sentido, porque é baseado em Node.

Você pode instalar globalmente com:

```bash
npm install -g @fission-ai/openspec@latest
```

Depois disso, entra no diretório do seu projeto e roda:

```bash
openspec init
```

Isso já configura o básico e prepara o projeto pra trabalhar com o fluxo do OpenSpec.

A partir daí, você não fica usando CLI direto o tempo todo — você passa a interagir com ele via comandos dentro do agente (tipo Claude Code, Codex, etc).

E aqui é onde entra a parte interessante.

O OpenSpec gira basicamente em três comandos:

```
/opsx:propose
/opsx:apply
/opsx:archive
```

E, sinceramente, só isso já resolve muita coisa.

A ideia é simples: você define o que quer fazer, implementa em cima disso e depois consolida o aprendizado.

Sem ficar criando um monte de etapa só pra parecer organizado.

---

## Como eu tenho usado no dia a dia

Quando vou começar uma mudança, eu uso o `/opsx:propose` pra descrever a intenção.

Algo tipo:

```
/opsx:propose adicionar filtro de status na listagem de pedidos
```


A partir disso, o OpenSpec já organiza a coisa pra mim: gera proposta, spec, design e tasks, tudo dentro de uma pasta `change`.

Isso aqui já resolve um problema grande, que é tirar a decisão da cabeça e colocar em algo explícito, um template.

Porque enquanto tá só na cabeça, cada pessoa (ou o próprio agente) interpreta de um jeito.

Depois disso, eu reviso. Não é porque a IA gerou que tá certo.

Aí sim eu parto pro `/opsx:apply`.

Nessa etapa, o agente segue as tasks e vai implementando passo a passo, sem eu precisar ficar guiando linha por linha.

E aqui tem uma diferença grande em relação ao jeito tradicional:

eu não tô mais pedindo código no escuro.  
eu tô executando um plano.

Quando termina, eu uso o `/opsx:archive`.

Isso pega tudo que foi feito, transforma em conhecimento permanente e atualiza as specs do projeto.

Na prática, isso resolve um problema que todo mundo já passou:

decisão que se perde com o tempo.

É tipo aquele dev que constrói um módulo inteiro e depois sai da empresa… e ninguém sabe direito como aquilo funciona.

Aqui, pelo menos, o conhecimento fica registrado.

---

## O que muda na prática

Sem isso, o fluxo é o clássico:

chega um card, o dev interpreta do jeito dele, começa a implementar, as dúvidas aparecem no meio do caminho e as decisões vão sendo tomadas no improviso.

Resultado: inconsistência, retrabalho e conhecimento espalhado.

Com o OpenSpec, a coisa fica mais alinhada:

você define a intenção, gera uma spec, implementa em cima disso e depois consolida o que foi feito.

Resultado: menos ambiguidade, mais previsibilidade e menos retrabalho.

---

## Onde ele faz mais sentido

Pelo que eu tenho usado até aqui, o OpenSpec funciona melhor quando:

você já sabe o que tá fazendo, o time é pequeno (ou você tá solo), e você quer velocidade sem abrir mão de controle.

Ele não tenta ser um processo completo de empresa. Ele é mais uma camada de organização.

E isso casa bem com a proposta dele:

leve, rápido e direto.

---

## Onde você precisa ter cuidado

Também não é mágica.

Se você escrever uma proposta ruim, a implementação vai ser ruim. Ele não resolve pensamento mal feito.

Outra coisa: pode parecer simples demais pra quem vem de processo mais rígido. Não tem tanta formalidade, nem tanta separação de papel.

E, claro, ainda exige revisão.

Spec não substitui olhar crítico.

---

## O que mudou pra mim

A principal mudança foi sair do Spec Kit e ir pro OpenSpec.

Não porque o Spec Kit seja ruim. Pelo contrário, ele me ajudou bastante a estruturar a forma de trabalhar com IA.

Mas, no meu uso, começou a ficar pesado demais.

Com o OpenSpec, eu consegui manter o que era mais importante pra mim — alinhar antes de implementar — só que de um jeito mais leve.

Menos overhead, menos verbosidade e mais fluidez no dia a dia.

Se quiser testar, tenta não complicar:

pega uma feature real, roda `/opsx:propose`, revisa, ajusta, roda `/opsx:apply` e depois `/opsx:archive`.

Só isso já muda bastante o jogo.

---

## Fechando

No fim das contas, OpenSpec não é sobre documentar.

É sobre alinhar.

Porque a IA não erra porque é burra.

Ela erra porque a gente não foi claro o suficiente.

E quando você melhora isso, tudo melhora junto:

o código, o processo e principalmente a frustração.

Pra mim, o ponto é esse.

Não parar de usar IA.

Mas parar de usar IA de qualquer jeito.

Obrigado por ficarem até aqui.