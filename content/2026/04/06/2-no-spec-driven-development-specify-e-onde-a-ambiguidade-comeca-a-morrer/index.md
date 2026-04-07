---
title: "No Spec-Driven Development, `specify` é onde a ambiguidade começa a morrer"
date: '2026-04-06T10:00:00-03:00'
slug: no-spec-driven-development-specify-e-onde-a-ambiguidade-comeca-a-morrer
tags:
  - ia
  - spec-driven-development
  - specify
  - especificacao
  - engenharia-de-software
draft: false
description: "Depois dos princípios, vem a hora de dizer com clareza o que precisa ser construído. Neste texto, eu explico por que a etapa de `specify` é a que transforma intenção vaga em trabalho executável."
---

# No Spec-Driven Development, `specify` é onde a ambiguidade começa a morrer

No texto [No Spec-Driven Development, tudo começa pelos princípios](/2026/04/10/no-spec-driven-development-tudo-comeca-pelos-principios/), eu foquei na etapa de `constitution`, que é onde eu defino os critérios que vão governar o projeto.

Mas princípio sozinho não entrega sistema.

Depois de dizer como o projeto deve pensar, chega a hora de dizer o que ele precisa construir.

É aí que entra a etapa de `specify`.

E, para mim, essa é uma das partes mais importantes de todo o fluxo. Porque, na prática, é aqui que começa o trabalho de uma nova demanda.

Antes de planejar, quebrar em tarefa ou implementar, eu preciso especificar o que aquela demanda realmente pede.

É justamente nesse ponto que a gente começa a trocar desejo genérico por expectativa operacional.

## O problema de pedir solução cedo demais

Quando alguém trabalha com agente de código com frequência, existe uma tentação muito forte de pular direto para a implementação.

A conversa costuma nascer assim:

> cria um CRUD para clientes  
> adiciona login  
> faz um dashboard  
> integra com pagamento  
> coloca notificação

De novo: isso não é necessariamente inútil. Em alguns casos, inclusive, dá para sair coisa boa daí.

O problema é que esse jeito de pedir mistura intenção, solução e expectativa num bolo só.

Eu digo "faz um dashboard", mas não deixo claro:

- para quem esse dashboard existe
- que problema ele resolve
- o que precisa aparecer ali
- o que é obrigatório nessa primeira versão
- o que está explicitamente fora de escopo
- como eu vou saber se aquilo ficou certo

Quando isso não está claro, o agente faz o que ele foi treinado para fazer: completa lacuna com uma solução plausível.

Só que plausível não é a mesma coisa que correta.

## O que a etapa de `specify` resolve

Eu não vejo `specify` como "escrever requisito bonitinho". Também não vejo como o momento de montar documentação pesada só porque o processo pede um artefato.

Para mim, `specify` serve para uma coisa bem concreta: reduzir ambiguidade suficiente para que a execução não precise adivinhar o problema.

É o momento em que eu tento deixar explícito:

- qual problema precisa ser resolvido
- quem é afetado por esse problema
- qual comportamento o sistema deve ter
- quais restrições importam
- o que entra e o que fica fora
- quais critérios definem se a entrega está aceitável

Ou seja, eu paro de falar em "ideia" e começo a falar em comportamento esperado.

Isso muda tudo.

Porque, quando a especificação está bem feita, o agente deixa de inventar contexto. Ele passa a trabalhar em cima de um terreno mais delimitado. Continua existindo interpretação, claro. Mas agora a interpretação acontece dentro de margens mais controladas.

## `Specify` não é detalhar a implementação

Esse ponto importa bastante.

Uma especificação ruim não é só aquela que está vaga demais. Também pode ser aquela que desce cedo demais para o nível da solução.

Exemplo de pedido ruim:

- criar endpoint `POST /users/register`
- usar Redis para sessão
- criar tabela X com colunas Y e Z
- implementar service `UserOnboardingService`

Perceba que isso já está quase no nível da implementação.

Às vezes isso é inevitável, principalmente quando já existe restrição técnica muito clara. Mas, em muitos casos, eu ainda não quero responder "como". Eu quero primeiro cravar "o que" precisa acontecer.

Algo como:

- um usuário novo precisa conseguir criar sua conta
- o sistema deve validar dados obrigatórios
- emails duplicados não podem ser aceitos
- após cadastro bem-sucedido, o usuário deve conseguir acessar a área autenticada

Agora sim eu tenho comportamento.

E comportamento é um ponto de partida muito melhor do que estrutura técnica prematura.

## O que eu tento capturar numa boa especificação

Eu não sigo um template rígido em toda situação, mas quase sempre tento responder um conjunto parecido de perguntas.

Não penso nisso como framework oficial. Penso mais como um filtro para saber se o pedido está claro o bastante para virar trabalho de verdade.

Normalmente eu quero sair da etapa de `specify` sabendo estas coisas:

- qual é o problema
- para quem ele existe
- qual resultado esperado importa
- qual é o escopo da primeira entrega
- quais restrições ou regras não podem ser ignoradas
- como validar se a entrega cumpriu o objetivo

Se eu não consigo responder isso com alguma objetividade, o pedido ainda está cru.

## As perguntas que eu costumo usar em `specify`

Se na `constitution` eu falei dos `5 Qs`, aqui eu tendo a usar outro conjunto de perguntas simples para forçar clareza.

Algo nessa linha:

- `Q1.` Qual problema real esta entrega resolve?
- `Q2.` Para quem esse comportamento existe?
- `Q3.` O que o sistema precisa fazer, exatamente?
- `Q4.` O que fica fora desta especificação?
- `Q5.` Como eu reconheço que isso está pronto?

### `Q1.` Qual problema real esta entrega resolve?

Essa pergunta existe para evitar feature ornamental.

Muita demanda chega com cara de solução, mas sem explicar a dor que está sendo atacada. Quando isso acontece, o risco é construir algo funcional e ainda assim irrelevante.

Se eu não consigo descrever o problema com clareza, geralmente ainda não tenho especificação. Tenho só impulso.

Uma resposta útil aqui costuma parecer algo como:

- hoje o time perde tempo consolidando dados manualmente
- o usuário não consegue concluir uma etapa importante sem apoio operacional
- existe retrabalho porque determinada informação fica espalhada

Esse tipo de formulação já tira a conversa do campo do "seria legal ter" e coloca no campo do "precisa resolver isto aqui".

### `Q2.` Para quem esse comportamento existe?

Essa pergunta ajuda a evitar especificação genérica demais.

Quando eu digo só "o usuário", normalmente estou escondendo detalhe importante. Usuário interno, cliente final, operador, administrador, financeiro, suporte: cada um desses papéis muda o que faz sentido construir.

Definir isso cedo ajuda porque várias decisões dependem de quem está do outro lado:

- nível de complexidade aceitável na interface
- volume de informação exibida
- tolerância a etapas manuais
- necessidade de auditoria
- tipo de erro que precisa ser tratado

Às vezes a mesma funcionalidade parece óbvia até a hora em que você pergunta "para quem?".

## `Q3.` O que o sistema precisa fazer, exatamente?

Aqui eu tento sair da linguagem genérica e descrever comportamento observável.

Não basta dizer "ter gestão de clientes". Isso ainda é nebuloso demais. Eu prefiro quebrar em ações e respostas mais concretas, por exemplo:

- permitir cadastrar cliente com campos obrigatórios definidos
- listar clientes com busca por nome ou documento
- impedir duplicidade por identificador principal
- permitir editar dados sem apagar histórico relevante

Esse tipo de escrita ajuda porque ela já nasce mais próxima da validação.

Se eu consigo imaginar alguém testando aquela frase, é um bom sinal.

Se eu leio a frase e ainda não sei o que seria considerado comportamento correto, a especificação ainda está frouxa.

### `Q4.` O que fica fora desta especificação?

Esse ponto é muito subestimado.

Escopo não é só o que entra. Escopo também é o que eu decido não resolver agora.

Quando eu não deixo isso explícito, o agente tende a completar o pacote. E, na cabeça dele, completar o pacote pode significar:

- criar permissões avançadas
- adicionar paginação, filtros e exportação
- preparar multitenancy
- estruturar internacionalização
- deixar tudo pronto para mobile

Nada disso é absurdo por si só. O problema é quando essas expansões aparecem porque ninguém disse "isso não faz parte desta entrega".

Então eu gosto de escrever exclusões de escopo sem vergonha nenhuma:

- nesta etapa não haverá controle fino de permissões
- relatórios analíticos ficam para uma próxima fase
- não será tratado suporte offline
- importação em lote está fora da primeira versão

Dizer "não" faz parte de especificar bem.

### `Q5.` Como eu reconheço que isso está pronto?

Para mim, essa é a pergunta que mais aproxima a especificação do trabalho executável.

Se eu não sei quais critérios encerram a entrega, eu abro espaço para duas coisas ruins: implementação infinita ou sensação falsa de conclusão.

Eu gosto de pensar nisso em termos de critérios de aceite mesmo. Não necessariamente num formato ultraformal, mas de um jeito que permita verificar o resultado sem depender de interpretação subjetiva demais.

Exemplos:

- dado um email já cadastrado, o sistema deve rejeitar nova criação com mensagem adequada
- após salvar um registro válido, ele deve aparecer na listagem
- apenas usuários autenticados podem acessar determinada área
- erro externo deve ser exibido sem quebrar o fluxo inteiro

Quando eu tenho esse nível de clareza, a próxima etapa fica muito mais segura.

## Especificação boa não precisa ser gigante

Vale dizer isso porque, quando alguém ouve "specify", pode imaginar um documento enorme, cheio de seções formais e texto corporativo.

Não é isso que eu estou defendendo.

Uma especificação pode ser enxuta e ainda assim ser muito boa, desde que responda o essencial com clareza.

O que eu tento evitar não é falta de volume. É falta de precisão.

Entre um texto curto e claro versus um texto longo e nebuloso, eu prefiro mil vezes o curto e claro.

## Um exemplo de diferença prática

Pedido genérico:

> criar módulo de pedidos

Isso abre espaço demais.

Agora olha uma versão mais especificada:

- operadores internos precisam registrar pedidos manualmente
- cada pedido deve estar associado a um cliente existente
- itens do pedido precisam informar quantidade e preço
- o sistema deve calcular total automaticamente
- pedidos não podem ser finalizados sem ao menos um item
- nesta primeira versão não haverá pagamento online nem emissão fiscal
- a entrega está pronta quando for possível criar, visualizar e consultar pedidos válidos sem cálculo manual

Ainda não descrevi arquitetura. Ainda não falei de banco, framework, fila, service ou naming de classe.

Mas agora já existe chão suficiente para planejar, implementar e revisar.

## No fim das contas

Se eu tivesse que resumir a função de `specify` em uma frase, eu diria isto: é a etapa em que a intenção deixa de ser vaga o bastante para virar conversa e fica clara o bastante para virar trabalho.

Para mim, esse é o ponto onde a ambiguidade começa a perder espaço de verdade.

Porque, no fundo, especificar bem não é produzir burocracia. É tornar o problema compreensível o suficiente para que implementação, revisão e validação trabalhem sobre a mesma realidade.

No próximo aprofundamento, o caminho natural é entrar na etapa que pega essa especificação e transforma em plano de execução.
