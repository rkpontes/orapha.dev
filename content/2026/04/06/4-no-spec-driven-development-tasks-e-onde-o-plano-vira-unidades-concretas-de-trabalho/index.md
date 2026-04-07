---
title: "No Spec-Driven Development, `tasks` é onde o plano vira unidades concretas de trabalho"
date: '2026-04-27T10:00:00-03:00'
slug: no-spec-driven-development-tasks-e-onde-o-plano-vira-unidades-concretas-de-trabalho
tags:
  - ia
  - spec-driven-development
  - tasks
  - tarefas
  - engenharia-de-software
draft: false
description: "Depois de definir princípios, especificar o problema e planejar a execução, chega a hora de quebrar o trabalho em partes concretas. Neste texto, eu explico por que a etapa de `tasks` é a que transforma estratégia em unidades executáveis."
---

# No Spec-Driven Development, `tasks` é onde o plano vira unidades concretas de trabalho

No texto [No Spec-Driven Development, tudo começa pelos princípios](/2026/04/10/no-spec-driven-development-tudo-comeca-pelos-principios/), eu foquei na etapa de `constitution`, em que eu defino os critérios que vão orientar as decisões do projeto.

Depois, em [No Spec-Driven Development, `specify` é onde a ambiguidade começa a morrer](/2026/04/17/no-spec-driven-development-specify-e-onde-a-ambiguidade-comeca-a-morrer/), eu entrei na fase em que a demanda deixa de ser intenção vaga e passa a ter comportamento esperado mais claro.

Na sequência, em [No Spec-Driven Development, `plan` é onde a especificação vira estratégia de execução](/2026/04/24/no-spec-driven-development-plan-e-onde-a-especificacao-vira-estrategia-de-execucao/), eu falei da etapa que organiza a travessia do trabalho com ordem, dependência e noção de risco.

Só que plano, por si só, ainda não é trabalho executável.

Entre saber a estratégia e começar a implementar, ainda existe uma pergunta importante: como eu transformo esse caminho em blocos concretos de execução sem perder coerência?

É aí que entra a etapa de `tasks`.

E, para mim, essa fase importa muito porque é nela que o planejamento deixa de ser uma boa narrativa sobre a execução e passa a virar partes de trabalho que alguém realmente consegue pegar, entender e concluir.

## O erro de achar que quebrar trabalho é só fazer checklist

Quando alguém escuta "tasks", é comum imaginar algo bem simples:

- criar backend
- criar frontend
- fazer testes
- revisar
- entregar

Isso até parece organização, mas muitas vezes ainda é genérico demais.

Uma lista assim pode dar a sensação de progresso estrutural sem resolver o principal: cada item ainda continua largo demais, ambíguo demais ou misturado demais para guiar bem a execução.

Na prática, tarefa mal quebrada costuma gerar alguns problemas bem conhecidos:

- blocos grandes demais para validar cedo
- partes com responsabilidade confusa
- itens que misturam várias decisões ao mesmo tempo
- dependências escondidas
- falsa sensação de que o trabalho está bem distribuído

Quando isso acontece, a execução começa a escorregar de novo para o improviso. A diferença é que agora o improviso vem embalado como checklist.

## O que a etapa de `tasks` resolve

Eu não vejo `tasks` como a obrigação de produzir uma lista enorme para parecer metódico. Também não vejo como a simples conversão do plano em subtítulos.

Para mim, `tasks` resolve uma coisa bem concreta: transformar a estratégia de execução em unidades de trabalho claras, limitadas e verificáveis.

É o momento em que eu tento decidir:

- qual pedaço do trabalho merece virar uma tarefa própria
- o que cada tarefa precisa entregar
- onde uma tarefa começa e termina
- quais dependências precisam estar explícitas
- que critério faz uma tarefa ser considerada concluída

Se `plan` organiza a travessia, `tasks` define os passos.

E isso importa muito porque, sem essa tradução, a implementação continua grande demais, difusa demais ou dependente demais de interpretação local.

## `Tasks` não é fragmentar por fragmentar

Tem um risco curioso aqui.

Quando a pessoa entende que precisa quebrar melhor o trabalho, ela pode exagerar para o outro lado e transformar tudo em microtarefas:

- criar model
- criar migration
- criar service
- criar controller
- criar rota
- criar teste unitário
- criar teste de integração

Isso pode funcionar em alguns contextos, mas muitas vezes produz uma quebra artificial demais.

Porque tarefa boa não é só tarefa pequena. Tarefa boa é tarefa com sentido.

Se eu separo o trabalho usando apenas cortes técnicos ou mecânicos, corro o risco de perder o vínculo com o comportamento que eu queria entregar. E, quando isso acontece, começo a otimizar pedaços de implementação em vez de unidades reais de resultado.

Para mim, a pergunta não é só "como dividir?". A pergunta é "como dividir sem destruir a coerência da entrega?".

## O que eu tento capturar numa boa etapa de `tasks`

Eu não sigo template rígido, mas normalmente quero sair dessa etapa com algumas coisas muito claras.

Algo nesta linha:

- cada tarefa precisa ter um objetivo compreensível
- cada tarefa deve produzir um resultado observável
- a fronteira entre tarefas não pode ser confusa
- dependências precisam estar explícitas
- o tamanho de cada bloco deve permitir validação razoável
- a sequência deve continuar respeitando o plano

Se eu olho para uma lista de tarefas e ainda sinto que "qualquer coisa pode significar qualquer coisa", então essa etapa ainda não fechou direito.

## As perguntas que eu costumo usar em `tasks`

Se na `constitution` eu usei os `5 Qs`, em `specify` outro conjunto de perguntas e em `plan` perguntas de ordem e risco, aqui eu costumo forçar clareza operacional.

Normalmente eu quero responder algo como:

- `Q1.` Qual unidade de trabalho produz um resultado real?
- `Q2.` Onde termina uma tarefa e começa a próxima?
- `Q3.` Que dependências precisam estar explícitas?
- `Q4.` O que eu consigo validar ao concluir cada tarefa?
- `Q5.` Essa quebra ajuda a executar ou só parece organizada?

### `Q1.` Qual unidade de trabalho produz um resultado real?

Essa pergunta existe para evitar tarefa ornamental.

Uma tarefa boa, para mim, precisa apontar para algum resultado que faça sentido por si só. Não necessariamente um resultado final para o usuário, mas pelo menos algo com função clara dentro da entrega.

Exemplos:

- estruturar o fluxo mínimo de criação de pedido com cliente obrigatório
- validar cálculo automático de total no backend
- permitir que operador visualize pedidos já registrados

Perceba a diferença.

Esses itens ainda podem envolver várias mudanças internas, mas continuam conectados a um resultado que dá para entender. Isso é bem melhor do que uma lista de pedaços técnicos sem contexto.

### `Q2.` Onde termina uma tarefa e começa a próxima?

Essa pergunta me ajuda a evitar sobreposição.

Quando a fronteira entre tarefas está ruim, várias coisas começam a acontecer:

- duas tarefas mexem no mesmo problema central
- critérios de conclusão ficam vagos
- uma tarefa parece "quase pronta" por tempo demais
- a revisão fica confusa porque ninguém sabe o que aquele bloco deveria ter resolvido

Eu gosto de tentar deixar a separação mais honesta. Se uma tarefa depende de outra para fazer sentido, isso precisa estar claro. Se duas tarefas estão resolvendo o mesmo núcleo, talvez a quebra esteja errada.

Em outras palavras: tarefa boa tem contorno.

### `Q3.` Que dependências precisam estar explícitas?

Nem toda tarefa nasce isolada.

Algumas precisam de decisão anterior, base mínima pronta ou validação concluída para fazer sentido. Quando isso fica implícito demais, a execução tende a abrir frentes cedo demais.

Então eu tento deixar visível:

- quais tarefas destravam outras
- o que pode andar em paralelo sem conflito alto
- quais itens dependem de modelo ou regra já estabilizada
- onde ainda existe ponto sensível demais para separar cedo

Isso é especialmente importante quando o trabalho envolve IA, porque abrir múltiplas execuções em paralelo sem dependência clara é um jeito eficiente de produzir colisão com aparência de produtividade.

### `Q4.` O que eu consigo validar ao concluir cada tarefa?

Essa pergunta aproxima muito `tasks` de execução saudável.

Para mim, uma tarefa fica muito melhor quando existe algum jeito claro de verificar se ela cumpriu o que prometia. Isso não significa que toda tarefa precise ter uma bateria formal de testes no mesmo instante, mas significa que ela precisa encostar em algum critério observável.

Algo como:

- o pedido pode ser criado com cliente e item válido
- o total é calculado corretamente
- o sistema bloqueia finalização sem item
- a listagem mostra pedidos recém-criados

Quando a tarefa não oferece nenhum ponto claro de verificação, geralmente ela está larga demais ou mal definida.

### `Q5.` Essa quebra ajuda a executar ou só parece organizada?

Essa é a pergunta que eu mais gosto porque ela desmonta muita falsa sofisticação.

Tem lista de tarefas que fica linda no papel, mas atrapalha mais do que ajuda. Às vezes porque criou blocos demais. Às vezes porque transformou cada camada técnica em um item próprio. Às vezes porque separou coisas que deveriam andar juntas.

Então eu tento ser pragmático.

Se a quebra:

- melhora a clareza de execução
- facilita validação
- reduz retrabalho
- preserva coerência com o plano

então ela está ajudando.

Se ela só aumenta a sensação de controle sem melhorar a travessia real do trabalho, provavelmente está sobrando.

## Um exemplo de diferença prática

Suponha a mesma demanda de pedidos que eu venho usando nos outros textos:

- operadores internos precisam registrar pedidos manualmente
- cada pedido deve estar associado a um cliente existente
- itens do pedido precisam informar quantidade e preço
- o sistema deve calcular total automaticamente
- pedidos não podem ser finalizados sem ao menos um item
- nesta primeira versão não haverá pagamento online nem emissão fiscal

Depois de especificar e planejar, eu ainda preciso transformar isso em trabalho executável.

Uma quebra fraca poderia ser:

- fazer backend de pedidos
- fazer frontend de pedidos
- criar testes

Isso é pouco útil. Cada item continua grande demais.

Agora olha uma quebra melhor:

- definir e validar a estrutura mínima do pedido com vínculo obrigatório a cliente
- implementar criação de pedido com cálculo automático de total
- bloquear finalização de pedido sem item válido
- disponibilizar visualização e consulta básica de pedidos para operadores
- cobrir os fluxos críticos e ajustar mensagens de erro

Aqui já existe bem mais chão.

Não porque a lista ficou mais longa, mas porque cada item aponta para uma unidade mais concreta de entrega.

## No fim das contas

Se eu tivesse que resumir a função de `tasks` em uma frase, eu diria isto: é a etapa em que o plano deixa de ser só sequência inteligente e passa a virar trabalho pegável.

Para mim, isso importa porque execução boa não depende só de saber para onde ir. Depende também de saber qual pedaço faz sentido atacar agora, com fronteira clara e critério de conclusão minimamente honesto.

Quando essa quebra está bem feita, a implementação ganha ritmo sem perder coerência.

No próximo texto, eu quero entrar na etapa de `implement`, que é quando toda essa cadeia finalmente vira código.
