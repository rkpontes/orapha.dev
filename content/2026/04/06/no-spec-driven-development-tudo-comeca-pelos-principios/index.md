---
title: "No Spec-Driven Development, tudo começa pelos princípios"
date: '2026-04-06T10:00:00-03:00'
slug: no-spec-driven-development-tudo-comeca-pelos-principios
tags:
  - ia
  - spec-driven-development
  - constitution
  - engenharia-de-software
  - principios
draft: false
description: "Antes de pensar em feature, eu prefiro definir os princípios que vão mandar no projeto. Neste texto, eu destrincho a etapa de constitution no SDD e os 5 Qs que uso para dar direção ao trabalho com IA."
---

# No Spec-Driven Development, tudo começa pelos princípios

No artigo [Como eu tenho usado Spec-Driven Development com o Spec Kit nos meus projetos](/2026/04/03/como-eu-tenho-usado-spec-driven-development-com-o-spec-kit-nos-meus-projetos/), eu passei pelas etapas do fluxo de forma mais geral.

Mas eu achei que valia a pena voltar com calma em cada uma delas, em textos separados, porque tem coisa ali que merece ser dissecada direito.

Se a ideia é aprofundar esse fluxo aos poucos, faz sentido abrir justamente pela etapa em que eu defino os princípios do projeto.

Estou falando da `constitution`.

E eu quero focar aqui menos na ferramenta em si e mais na lógica por trás da coisa. Porque, sinceramente, o nome pode mudar, o comando pode mudar, a stack pode mudar, mas a necessidade continua a mesma: antes de sair pedindo feature para agente, alguém precisa dizer quais são as regras que vão governar as decisões daquele projeto.

Para mim, esse é um dos pontos mais subestimados quando a gente fala de desenvolvimento com IA.

## O erro de começar pela feature

O caminho mais natural, principalmente quando a pessoa já está acostumada a usar agente de código, é começar assim:

> cria uma tela de cadastro  
> faz uma API para tal coisa  
> adiciona autenticação  
> agora cria testes  
> agora refatora  
> agora melhora a arquitetura

Perceba o padrão: a conversa começa sempre pela entrega visível.

Não é que isso seja sempre errado. Em projeto pequeno, experimento rápido ou prova de conceito, dá até para ir nessa linha e aceitar o caos controlado. O problema é quando essa lógica vira método de trabalho.

Quando eu começo direto pela feature, sem declarar antes os princípios do projeto, eu deixo uma parte importante da decisão nas mãos do improviso. E agente é muito bom em completar lacuna. Bom até demais. Se eu não digo com clareza o que valorizo, ele vai preencher o vazio com padrão genérico, suposição plausível e excesso de boa vontade.

É aí que começa a desandar.

O agente cria abstração demais em projeto simples. Ou faz tudo acoplado demais em projeto que precisava durar. Ou enfia testes onde não era prioridade. Ou ignora teste onde era obrigatório. Ou inventa uma arquitetura "bonita" que ninguém pediu. Ou toma decisão de naming, organização e estrutura sem nenhum alinhamento com o que eu realmente queria preservar.

No fim, a sensação é de produtividade. Mas muitas vezes é só velocidade sem direção.

## O que a `constitution` resolve de verdade

Quando eu falo em `constitution`, não estou pensando em documento burocrático. Não é para virar manifesto bonito de time que ninguém lê depois. Também não é para escrever um tratado abstrato sobre boas práticas.

A função dessa etapa é muito mais prática: declarar os princípios que vão orientar as próximas decisões.

Em outras palavras, é o momento em que eu digo:

- o que este projeto valoriza
- o que este projeto evita
- quais critérios pesam mais quando houver trade-off
- como qualidade será interpretada aqui
- que tipo de complexidade é aceitável e qual já é exagero

E isso não fica restrito a estilo de código ou arquitetura. Dependendo do contexto, eu também posso usar a `constitution` para registrar regras operacionais do projeto, como fluxo de branch, política de testes e exigências mínimas de segurança. Se essas coisas mudam a forma como a entrega deve ser construída e revisada, faz sentido que elas apareçam logo aqui.

Isso muda a conversa inteira.

Porque, a partir daí, a IA deixa de responder apenas ao pedido imediato e passa a operar dentro de um campo de restrições e preferências mais explícito. E, para mim, trabalhar com IA sem restrição clara é pedir para receber uma solução tecnicamente possível, mas conceitualmente desalinhada.

## Princípio não é regra solta

Tem uma diferença importante aqui.

Muita gente, quando pensa em princípios, escreve coisas muito genéricas:

- usar clean code
- manter qualidade
- seguir boas práticas
- fazer código escalável

Isso parece bonito, mas ajuda pouco.

Essas frases até apontam uma direção, só que ainda deixam espaço demais para interpretação. E, quando existe espaço demais para interpretação, o agente preenche com o que ele conhece como padrão médio. O problema é que padrão médio não é contexto.

Para mim, princípio bom é princípio que influencia decisão real.

Por exemplo, em vez de dizer só "manter simplicidade", eu prefiro algo mais concreto, como:

- priorizar solução simples antes de abstração reutilizável
- evitar camadas extras enquanto o domínio ainda for pequeno
- só introduzir padrão mais sofisticado quando houver dor concreta

Agora sim existe uma orientação que impacta o que vai ser construído.

Da mesma forma, em vez de dizer apenas "garantir qualidade", eu posso dizer:

- toda entrega deve preservar legibilidade
- nomes precisam comunicar intenção de negócio
- mudanças não devem quebrar comportamento existente sem motivo explícito
- testes automatizados são obrigatórios apenas nas partes críticas

Isso já muda bastante o comportamento esperado.

## A `constitution` existe para segurar o eixo do projeto

Quanto mais eu uso agente, mais eu percebo que o maior risco não é ele errar sintaxe. Isso normalmente é o menor dos problemas.

O risco maior é ele acertar o código e errar a direção.

Essa distinção importa muito.

Um sistema pode compilar, passar na build, rodar localmente e ainda assim estar tecnicamente desalinhado com o que o projeto precisava ser. Pode estar complicado demais, frágil demais, acoplado demais, genérico demais, ou simplesmente fora do espírito da base.

É por isso que eu vejo a `constitution` como uma etapa de alinhamento de critérios mesmo. É nela que eu estabeleço como o projeto pensa.

Pode parecer um jeito pomposo de dizer isso, mas é exatamente esse o ponto: antes de decidir o que fazer, eu preciso definir como as decisões serão tomadas.

Sem isso, cada feature vira uma nova negociação improvisada.

## O que eu costumo definir nessa etapa

Eu não sigo uma fórmula rígida, mas normalmente tento responder o que, na minha cabeça, virou uma espécie de `5 Qs` da `constitution`.

Não é framework formal nem método patenteado. É só um jeito simples de não deixar essa etapa vaga demais.

Para mim, esse é um jeito bom de sair do princípio genérico e chegar em algo que realmente orienta decisão.

Os `5 Qs` que eu costumo responder são estes:

- `Q1.` Que tipo de solução este projeto deve privilegiar agora?
- `Q2.` Que cara esse código precisa ter para continuar legível?
- `Q3.` Quais limites técnicos não podem ser negociados?
- `Q4.` Que nível de teste faz sentido nesta fase?
- `Q5.` Quanta arquitetura este projeto realmente precisa neste momento?

### `Q1.` Que tipo de solução este projeto deve privilegiar agora?

Essa pergunta existe para definir o grau de sofisticação aceitável.

Todo projeto vive essa tensão. Se eu simplifico demais, talvez a próxima mudança doa. Se eu preparo demais para o futuro, corro o risco de montar uma estrutura pesada para um problema pequeno. Então eu gosto de dizer explicitamente para que lado o projeto deve pender.

Na prática, responder isso é dizer coisas como:

- priorizar solução direta antes de abstrações reutilizáveis
- preparar crescimento só quando houver sinal concreto dessa necessidade
- evitar camadas extras enquanto o domínio ainda for pequeno

Em geral, eu tendo a favorecer simplicidade com crescimento consciente. Ou seja: faz simples agora, mas sem fazer de qualquer jeito.

### `Q2.` Que cara esse código precisa ter para continuar legível?

Nem toda clareza é só questão de código bonito. Muitas vezes, clareza tem mais a ver com comunicação do que com estilo.

Nessa parte, eu tento dizer como o código precisa se apresentar. Se os nomes devem refletir o domínio, se a organização deve ser direta, se a leitura deve ser mais importante que qualquer truque esperto, tudo isso cabe aqui.

Uma forma prática de responder é escrever coisas como:

- nomes devem comunicar intenção de negócio
- a estrutura deve ser fácil de entender por outra pessoa do time
- legibilidade pesa mais do que esperteza técnica

Isso é importante porque IA consegue gerar muita coisa rapidamente, mas nem sempre com o melhor senso de comunicação. Às vezes a solução até funciona, mas o texto do código fica genérico, sem vocabulário do domínio, sem cara de sistema bem pensado.

### `Q3.` Quais limites técnicos não podem ser negociados?

Essa é a pergunta que define limite.

Toda constituição precisa deixar claro o que o projeto não aceita, mesmo quando isso parecer mais rápido no curto prazo. É aqui que eu costumo registrar o tipo de atalho que não vale a pena, a complexidade que não quero comprar e o tipo de decisão que precisa de justificativa antes de entrar.

Exemplos de resposta:

- não introduzir dependência sem necessidade forte
- não aumentar complexidade só para parecer escalável
- não quebrar compatibilidade sem justificar
- não sacrificar entendimento em nome de esperteza técnica

Também é aqui que eu posso deixar travas bem práticas, por exemplo:

- o projeto deve seguir um fluxo de `gitflow` ou outra estratégia de branches definida pelo time
- toda mudança em fluxo crítico precisa vir acompanhada do tipo de teste combinado para este projeto
- requisitos mínimos de segurança, como autenticação obrigatória, controle de acesso, proteção de segredos e cuidado com dependências, não podem ser tratados como detalhe opcional

Esse tipo de princípio ajuda muito porque reduz a chance de o agente confundir sofisticação com qualidade.

### `Q4.` Que nível de teste faz sentido nesta fase?

Esse ponto varia muito de projeto para projeto. E justamente por variar tanto, vale estar na constituição.

Tem projeto em que eu quero cobertura séria desde o começo. Tem projeto em que eu aceito não ter teste automatizado na primeira versão para ganhar velocidade. Tem contexto em que integração é mais importante que teste unitário. Tem contexto em que o domínio exige muito mais rigor.

Então eu tento responder de forma bem objetiva:

- testes automatizados são obrigatórios ou não?
- se forem, onde eles são indispensáveis?
- nesta fase, vale mais teste unitário, integração ou validação manual bem guiada?

O importante é não deixar isso subentendido. Se teste é obrigatório, diga. Se teste é seletivo, diga. Se nesta fase não faz sentido investir nisso, diga também. O que eu tento evitar é deixar a IA adivinhar a política de qualidade do projeto.

Para mim, essa mesma lógica vale para segurança. Se o projeto precisa seguir requisitos mínimos de cybersegurança desde a primeira entrega, isso deve ser dito na `constitution` com a mesma objetividade. Autorização, auditoria, tratamento de segredo, proteção de dado sensível e critérios básicos de hardening não deveriam aparecer só no fim como correção tardia.

### `Q5.` Quanta arquitetura este projeto realmente precisa neste momento?

Essa pergunta me ajuda a conter a tentação de transformar qualquer projeto em vitrine de arquitetura.

Nem todo projeto precisa de DDD completo, event-driven architecture, filas, mensageria, plugin system, modularização extrema e quinze interfaces para abstrair meia dúzia de regra simples.

Quando eu respondo essa pergunta, normalmente faço isso delimitando o que é aceitável agora e o que seria prematuro neste momento.

Exemplo:

- manter arquitetura enxuta nesta fase
- evitar padrões avançados sem necessidade concreta
- preferir organização simples até que a complexidade do domínio justifique algo maior

Quando eu percebo que o projeto precisa se manter leve, eu escrevo isso de forma direta. Sem cerimônia. Porque, se eu não escrever, existe uma boa chance de aparecer arquitetura de congresso em problema de esquina.

## Um exemplo de raciocínio

Suponha um projeto pequeno, interno, com prazo curto, para resolver um problema operacional bem específico.

Se eu não digo nada sobre os princípios, o agente pode:

- criar separações excessivas
- preparar o sistema para uma escala que talvez nunca venha
- sugerir muitas bibliotecas
- investir em abstrações genéricas cedo demais

Agora imagine que eu defino algo mais ou menos assim:

- priorizar simplicidade e velocidade de manutenção
- evitar dependências desnecessárias
- preferir estrutura direta enquanto o domínio for pequeno
- garantir clareza de nomes e fluxo
- testes automatizados apenas nas regras mais críticas
- seguir o fluxo de branch definido pelo time, sem pular revisão
- tratar autenticação, autorização e segredos como requisitos obrigatórios desde o início

Perceba como isso já muda o terreno.

Não estou definindo a feature. Não estou dizendo se vai ser API, tela, banco ou framework. Estou definindo o jeito de pensar aquele projeto. E isso, mais na frente, afeta naming, organização de pasta, número de camadas, estratégia de validação, critérios de refatoração e até o tipo de sugestão que a IA vai considerar aceitável.

## Isso também é engenharia de software

Tem gente que olha para essa etapa e pensa que isso é só "prompt melhorado". Eu acho uma leitura fraca.

Para mim, isso é engenharia de software aplicada a um novo contexto de execução.

No fundo, estamos falando da mesma responsabilidade de sempre:

- definir critérios antes de construir
- reduzir ambiguidade
- explicitar trade-offs
- proteger a qualidade do sistema

A diferença é que agora isso precisa ser dito de um jeito que um agente consiga usar ao longo do fluxo.

Ou seja: não basta ter bom senso na cabeça. É preciso transformar esse bom senso em instrução operacional.

## No fim das contas

Se eu tivesse que resumir a importância da `constitution` em uma frase, eu diria o seguinte: ela existe para impedir que a execução comece sem critério.

No SDD, isso importa porque a ideia não é só produzir artefato. É produzir com intenção.

E intenção, quando não é declarada, vira suposição.

É por isso que eu gosto tanto dessa etapa. Antes de discutir tela, endpoint, banco, stack ou tarefa, eu consigo definir o que realmente vai mandar nas decisões.

Para mim, esse é o momento em que o projeto deixa de ser apenas um pedido e começa a virar um sistema com identidade técnica.

No próximo aprofundamento, o caminho natural é entrar na etapa de `specify`, que é quando a conversa sai dos princípios e entra naquilo que de fato precisa ser construído.
