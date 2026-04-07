---
title: "No Spec-Driven Development, `plan` é onde a especificação vira estratégia de execução"
date: '2026-04-06T10:00:00-03:00'
slug: no-spec-driven-development-plan-e-onde-a-especificacao-vira-estrategia-de-execucao
tags:
  - ia
  - spec-driven-development
  - plan
  - planejamento
  - engenharia-de-software
draft: false
description: "Depois de definir princípios e especificar o problema, chega a hora de planejar a execução. Neste texto, eu explico por que a etapa de `plan` é a que transforma especificação clara em caminho viável de implementação."
---

# No Spec-Driven Development, `plan` é onde a especificação vira estratégia de execução

No texto [No Spec-Driven Development, tudo começa pelos princípios](/2026/04/10/no-spec-driven-development-tudo-comeca-pelos-principios/), eu falei da etapa de `constitution`, em que eu defino os critérios que vão orientar o projeto.

Depois, em [No Spec-Driven Development, `specify` é onde a ambiguidade começa a morrer](/2026/04/17/no-spec-driven-development-specify-e-onde-a-ambiguidade-comeca-a-morrer/), eu entrei na etapa em que a demanda deixa de ser intenção vaga e passa a ter comportamento esperado mais claro.

Só que ainda falta uma ponte importante entre entender o problema e sair implementando.

Essa ponte é a etapa de `plan`.

E, para mim, ela existe para responder uma pergunta simples: dado que agora eu sei o que precisa ser feito, qual é o melhor jeito de atravessar esse trabalho sem transformar a execução num improviso caro?

Porque uma coisa é ter uma especificação boa. Outra coisa é saber executar aquela especificação com ordem, critério e noção de dependência.

É aí que muita demanda começa a se perder.

## O erro de achar que especificação boa já basta

Quando a especificação está clara, dá uma sensação meio enganosa de que o trabalho já está praticamente resolvido.

O raciocínio costuma ser este:

> agora que está tudo claro, é só implementar  
> a IA já entendeu o que precisa fazer  
> vamos sair quebrando em prompt e entregar logo

Em projeto muito pequeno, às vezes isso até funciona. Mas, conforme a demanda cresce um pouco, esse salto começa a cobrar preço.

Porque entender o que precisa ser construído não resolve automaticamente:

- por onde começar
- o que depende do quê
- o que pode ser feito em paralelo
- que parte concentra mais risco
- onde vale validar cedo
- como evitar retrabalho entre etapas

Sem esse raciocínio, a implementação vira uma sequência de ações localmente plausíveis, mas globalmente desorganizadas.

No curto prazo, parece rapidez.

No médio prazo, aparece refação, colisão de decisões, escopo torto e a famosa sensação de que o trabalho andou muito e consolidou pouco.

## O que a etapa de `plan` resolve

Eu não vejo `plan` como cronograma pomposo. Também não vejo como a obrigação de montar um documento cheio de caixinhas só para parecer processo.

Para mim, `plan` resolve uma coisa bem prática: transformar uma especificação em estratégia de execução.

É o momento em que eu tento organizar:

- a ordem do trabalho
- as dependências entre partes
- os blocos que fazem sentido separar
- os riscos que merecem atenção cedo
- a sequência que reduz retrabalho
- os pontos de validação ao longo do caminho

Em outras palavras, se `specify` responde "o que precisa acontecer", `plan` começa a responder "como eu organizo a travessia desse trabalho".

Isso não significa descer para código ainda. Significa dar forma operacional ao caminho.

## `Plan` não é sair distribuindo tarefa no impulso

Tem um erro comum aqui.

Muita gente entende planejamento como simplesmente quebrar a demanda em vários itens menores:

- fazer backend
- fazer frontend
- criar banco
- adicionar testes
- revisar

Isso é melhor do que nada, mas ainda pode ser superficial demais.

Porque planejar não é só fragmentar. É organizar com intenção.

Uma boa quebra de trabalho precisa considerar dependência, risco e sequência lógica. Senão eu só troco um bloco grande por vários bloquinhos confusos.

Por exemplo, se existe uma decisão estrutural que impacta API, interface e persistência, talvez o primeiro passo não seja "fazer tela". Talvez seja validar primeiro o fluxo principal, o modelo de dados ou a regra central. Se eu ignoro isso, eu espalho implementação antes de travar o eixo da solução.

Planejamento bom, para mim, não é a lista mais longa. É a ordem mais defensável.

## O que eu tento capturar numa boa etapa de `plan`

Eu não sigo um template rígido, mas normalmente quero sair dessa etapa com algumas coisas relativamente claras.

Algo nesta linha:

- qual é o caminho de execução mais seguro
- quais partes destravam as outras
- que blocos podem ser tratados separadamente
- onde está o maior risco técnico ou de entendimento
- em que momento vale validar antes de continuar
- como evitar trabalho redundante ou sequência ruim

Se eu ainda não consigo enxergar isso, a demanda pode até estar bem especificada, mas ainda não está bem planejada.

## As perguntas que eu costumo usar em `plan`

Se na `constitution` eu falei dos `5 Qs`, e em `specify` eu usei outro conjunto para reduzir ambiguidade, em `plan` eu tendo a fazer perguntas que forçam ordem e estratégia.

Normalmente eu quero responder algo como:

- `Q1.` Qual é a menor sequência viável para colocar essa entrega em pé?
- `Q2.` O que depende do quê?
- `Q3.` Onde está o maior risco ou incerteza?
- `Q4.` O que precisa ser validado antes de expandir?
- `Q5.` Como quebrar isso sem perder coerência?

### `Q1.` Qual é a menor sequência viável para colocar essa entrega em pé?

Essa pergunta me ajuda a não começar pelo lugar mais vistoso, e sim pelo lugar mais útil.

Nem sempre o primeiro passo é o mais visível. Às vezes o trabalho precisa começar por uma base mínima que permita o restante existir com menos atrito.

Quando eu respondo isso, eu tento pensar em algo como:

- qual é o fluxo principal que precisa existir primeiro
- que fundação mínima sustenta as próximas etapas
- o que eu preciso ter de pé para parar de especular e começar a consolidar

Isso ajuda muito a evitar planejamento ornamental, em que várias peças paralelas avançam sem que o núcleo do problema esteja realmente resolvido.

### `Q2.` O que depende do quê?

Essa é a pergunta que impede o plano de virar wishful thinking.

Tem demanda em que quase tudo parece poder acontecer em paralelo, até a hora em que uma decisão muda e arrasta metade do trabalho junto.

Eu gosto de deixar explícito:

- quais partes são pré-requisito para outras
- que decisões precisam ser tomadas cedo
- o que pode avançar em paralelo sem risco alto de colisão
- onde existe acoplamento suficiente para exigir sequência

Isso é especialmente importante quando a execução envolve IA, porque é muito fácil abrir várias frentes ao mesmo tempo e só depois perceber que elas estavam compartilhando pressupostos diferentes.

### `Q3.` Onde está o maior risco ou incerteza?

Planejar também é decidir onde eu não quero descobrir problema tarde demais.

Toda demanda tem algum ponto mais sensível:

- regra de negócio ainda meio nebulosa
- integração externa mais instável
- decisão de modelagem que afeta o resto
- restrição técnica que pode travar a implementação

Se eu identifico isso cedo, eu consigo puxar esse risco para mais perto do início. Não necessariamente para resolvê-lo completamente de cara, mas pelo menos para validá-lo antes que o restante do plano seja construído em cima de uma suposição fraca.

Para mim, esse é um dos maiores ganhos de `plan`: ele reduz a chance de sequência bonita em cima de premissa errada.

### `Q4.` O que precisa ser validado antes de expandir?

Nem tudo precisa ser implementado até o fim antes de aprender alguma coisa útil.

Às vezes eu só preciso validar:

- se o fluxo central fecha
- se a regra principal se sustenta
- se a integração responde como esperado
- se a modelagem inicial não está torta

Essa pergunta me ajuda a inserir marcos de validação dentro do plano, em vez de empurrar toda a aprendizagem para o fim.

Isso vale especialmente em trabalho com agente, porque a velocidade de produção pode mascarar um problema estrutural por várias interações seguidas. Quando eu crio pontos de validação, eu controlo melhor esse risco.

### `Q5.` Como quebrar isso sem perder coerência?

Quebrar trabalho é necessário. Quebrar mal é perigosíssimo.

Se eu separo demais, crio fragmentação e overhead. Se separo de menos, volto ao bloco grande e difícil de controlar.

Então eu tento buscar uma decomposição que preserve sentido. Algo em que cada bloco tenha uma responsabilidade clara, um critério de conclusão razoável e uma relação compreensível com o objetivo maior.

Na prática, isso costuma significar:

- quebrar por fluxo ou capacidade, não por camada arbitrária
- evitar dividir cedo demais algo que ainda depende de decisão central
- separar o que pode ser validado isoladamente
- manter cada parte conectada a um resultado observável

Quando isso fica bem feito, a etapa seguinte ganha muito. Porque a execução passa a andar em trilhos mais estáveis.

## Um exemplo de diferença prática

Especificação já clara:

- operadores internos precisam registrar pedidos manualmente
- cada pedido deve estar associado a um cliente existente
- itens do pedido precisam informar quantidade e preço
- o sistema deve calcular total automaticamente
- pedidos não podem ser finalizados sem ao menos um item
- nesta primeira versão não haverá pagamento online nem emissão fiscal

Até aqui, eu sei o que precisa ser construído.

Mas isso ainda não é um plano.

Uma quebra fraca poderia ser:

- fazer tela de pedidos
- criar endpoint de pedidos
- salvar no banco
- adicionar testes

Isso parece organizado, mas ainda é uma lista genérica.

Agora olha uma versão mais planejada:

- validar modelo mínimo do pedido e a relação obrigatória com cliente
- implementar criação de pedido com cálculo automático de total
- impedir finalização de pedido sem item válido
- só depois construir listagem e visualização para operadores
- por fim, cobrir os fluxos críticos e ajustar mensagens de erro

Perceba a diferença.

Na segunda versão, eu não estou só dividindo trabalho. Eu estou escolhendo uma ordem que respeita dependência, reduz retrabalho e prioriza o núcleo da regra antes das camadas em volta.

## Planejar não é burocratizar

Vale dizer isso porque muita gente torce o nariz quando escuta a palavra "planejamento".

Eu também não tenho paciência para processo que existe só para gerar documento.

Mas a etapa de `plan` que eu estou defendendo aqui é outra coisa. Ela não serve para engessar o trabalho. Serve para aumentar a chance de execução limpa.

Antes da IA, boa parte da energia do desenvolvimento era consumida pela própria codificação. Tinha muito mais hora operacional indo para escrever, ajustar, refatorar, conectar partes e carregar a implementação no braço.

Com a IA, esse tempo de codificar caiu de forma brusca.

E, se esse tempo caiu, ele não deveria ser automaticamente reinvestido em produzir ainda mais código no impulso.

Para mim, uma parte relevante desse tempo precisa ser realocada para planejamento.

Não no sentido de transformar desenvolvedor em PM ou PO.

Não é sobre substituir quem define prioridade, contexto de negócio, objetivo de produto ou direção da demanda.

É sobre outra coisa: uma vez que a demanda já chegou, alguém ainda precisa pensar qual é a melhor forma de executá-la.

Alguém ainda precisa entender:

- qual é a melhor ordem
- onde não vale improvisar
- o que precisa ser validado cedo
- como dividir o trabalho sem perder o fio da meada

Antes, muita ineficiência ficava escondida dentro do esforço manual de implementação. Agora que implementar ficou mais barato, ficou mais visível o peso de uma execução mal pensada.

Se eu recebo uma demanda boa e mesmo assim saio codando sem plano, a chance não é só de errar. É de errar rápido, em várias frentes, com uma falsa sensação de produtividade.

Então, para mim, planejar bem virou uma habilidade ainda mais importante no contexto de IA.

Não porque o processo ficou mais burocrático.

Mas porque a codificação deixou de ser o principal gargalo. E, quando isso acontece, pensar melhor a execução passa a ter retorno muito maior.

## Fechando

Se a `constitution` define os princípios, e `specify` reduz ambiguidade sobre o que precisa ser construído, então `plan` é a etapa que transforma essa clareza em movimento coordenado.

É onde eu paro de olhar apenas para a demanda e começo a olhar para a travessia.

Porque execução não é só fazer. Execução também é escolher a ordem certa para fazer.

E, no fim, muita implementação ruim não nasce de especificação ruim. Nasce de sequência ruim.

No próximo texto, eu quero entrar na etapa de `tasks`, que é quando esse plano começa a virar unidades concretas de trabalho.
