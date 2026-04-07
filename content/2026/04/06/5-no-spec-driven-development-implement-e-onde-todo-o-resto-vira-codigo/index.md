---
title: "No Spec-Driven Development, `implement` é onde todo o resto vira código"
date: '2026-05-08T10:00:00-03:00'
slug: no-spec-driven-development-implement-e-onde-todo-o-resto-vira-codigo
tags:
  - ia
  - spec-driven-development
  - implement
  - implementacao
  - engenharia-de-software
draft: false
description: "Depois de definir princípios, especificar o problema, planejar a execução e quebrar o trabalho em tarefas, chega a hora de implementar. Neste texto, eu explico por que implementar pode até ser a parte mais direta, mas o trabalho real está em revisar e validar o que foi entregue."
---

# No Spec-Driven Development, `implement` é onde todo o resto vira código

No texto [No Spec-Driven Development, tudo começa pelos princípios](/2026/04/10/no-spec-driven-development-tudo-comeca-pelos-principios/), eu falei da etapa de `constitution`, em que eu defino os princípios que vão governar as decisões do projeto.

Depois, em [No Spec-Driven Development, `specify` é onde a ambiguidade começa a morrer](/2026/04/17/no-spec-driven-development-specify-e-onde-a-ambiguidade-comeca-a-morrer/), eu mostrei o ponto em que a demanda ganha comportamento esperado mais claro.

Na sequência, em [No Spec-Driven Development, `plan` é onde a especificação vira estratégia de execução](/2026/04/24/no-spec-driven-development-plan-e-onde-a-especificacao-vira-estrategia-de-execucao/), eu entrei na etapa que organiza a travessia com ordem, dependência e noção de risco.

Depois disso, em [No Spec-Driven Development, `tasks` é onde o plano vira unidades concretas de trabalho](/2026/05/01/no-spec-driven-development-tasks-e-onde-o-plano-vira-unidades-concretas-de-trabalho/), eu falei da quebra que transforma estratégia em blocos executáveis.

Só que, em algum momento, tudo isso precisa virar código.

É aí que entra `implement`.

E aqui eu acho que vale uma simplificação importante: sim, em certo sentido, `implement` é só implementar.

Se o trabalho anterior foi bem feito, esta etapa não deveria carregar um grande drama metodológico. O objetivo agora é pegar uma tarefa já delimitada e transformar aquilo em código.

Só que isso não significa que o trabalho acabou.

No contexto de IA, muitas vezes o ato de implementar ficou barato. O agente escreve rápido, sugere estrutura, conecta partes e devolve uma solução plausível em pouco tempo.

Por isso, para mim, o ponto principal de `implement` não é romantizar a escrita do código.

O ponto principal é outro: depois que o código foi gerado, alguém ainda precisa revisar o que foi entregue.

## Implementar pode ser a parte mais fácil

Dependendo do contexto, a implementação em si quase vira uma etapa operacional:

> pega a tarefa  
> gera o código  
> ajusta o necessário  
> segue adiante

Se `constitution`, `specify`, `plan` e `tasks` fizeram o trabalho direito, isso é até esperado.

O problema começa quando a pessoa trata a saída do agente como se ela já fosse a entrega final.

Porque uma coisa é gerar código.

Outra coisa é verificar se aquele código:

- resolveu exatamente a tarefa
- respeitou o escopo
- não inventou coisa fora do combinado
- não distorceu o comportamento especificado
- continua coerente com os princípios do projeto

É aí que, para mim, mora o trabalho de verdade.

## O que realmente importa depois de implementar

Eu tendo a olhar para `implement` menos como um momento épico de construção e mais como um ponto de transição.

O código apareceu. Agora ele precisa ser confrontado com o que veio antes.

Na prática, eu quero revisar se a entrega:

- corresponde à tarefa que foi pedida
- continua fiel à especificação
- não atropelou o plano
- não trouxe complexidade desnecessária
- pode ser aceita com confiança razoável

Se eu termino essa etapa só com a sensação de que "parece que ficou bom", ainda é pouco.

## Um exemplo de diferença prática

Vamos voltar ao exemplo dos pedidos.

Suponha que a tarefa atual seja esta:

- implementar criação de pedido com cálculo automático de total

Se eu olhar só para a etapa de geração, talvez baste pedir para o agente fazer isso e receber um bloco de código de volta.

Mas o trabalho relevante começa logo depois:

- ele criou apenas o fluxo de criação ou inventou mais coisa?
- o total está sendo calculado do jeito certo?
- pedido sem item continua bloqueado?
- a relação com cliente existente foi respeitada?
- a solução ficou compatível com a simplicidade que o projeto queria?

Perceba a diferença.

O ato de implementar pode até ser direto.

O que não pode ser automático é a aceitação daquilo que foi implementado.

## No fim das contas

Depois que a entrega estiver finalizada, ainda existe uma responsabilidade importante na sua mão: garantir que tudo aquilo que foi definido como requisito realmente foi atendido. Não basta olhar para o código e sentir que ele parece pronto. Também não basta confiar só porque a implementação saiu limpa, organizada ou plausível.

Se existem arquivos de `requirements.md` envolvidos naquele trabalho, cabe a você conferir um por um e garantir que todos os itens listados ali foram, de fato, resolvidos e marcados como concluídos. Isso importa porque, no fim, o que valida a entrega não é só a existência do código, mas a aderência entre o que foi pedido e o que realmente foi entregue.

E tem outro ponto aqui que eu acho importante: nem tudo vai ser validado automaticamente. Em vários casos, ainda vai existir checagem manual. Fluxo de interface, comportamento em cenário específico, integração que depende de contexto real, detalhe de experiência ou qualquer outra coisa que não esteja totalmente coberta por teste automatizado ainda precisa ser verificada por você.

Ou seja: a etapa de `implement` não termina exatamente quando o código aparece. Ela termina quando a entrega foi revisada, confrontada com os requisitos e validada de forma minimamente responsável.

Mas, no fim das contas, o fluxo não termina como quem fecha um processo engessado e vai embora. Ele termina e recomeça.

Se surgir uma nova demanda, o caminho natural é voltar para `specify` e começar de novo a partir dali, com uma nova especificação clara para aquilo que precisa ser construído agora. E, se no meio desse caminho você perceber que algum princípio da `constitution` precisa mudar, ser refinado ou até ser substituído, isso também faz parte do processo.

Eu gosto dessa estrutura justamente porque ela não é rígida no mau sentido. Ela é atômica. Cada parte existe com uma função clara, mas nenhuma delas precisa ser tratada como peça sagrada ou imutável. Se o projeto evolui, a estrutura pode evoluir junto. Se o contexto muda, os princípios podem mudar junto. Se a forma de executar melhora, o fluxo também pode ser ajustado.

Para mim, esse é um dos pontos mais fortes dessa abordagem: ela organiza o trabalho sem fingir que o projeto vai permanecer igual para sempre.

Obrigado por ler até aqui.
