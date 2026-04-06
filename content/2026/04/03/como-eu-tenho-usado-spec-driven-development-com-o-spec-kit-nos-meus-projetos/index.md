---
title: "Como eu tenho usado Spec-Driven Development com o Spec Kit nos meus projetos"
date: '2026-04-03T10:00:00-03:00'
slug: como-eu-tenho-usado-spec-driven-development-com-o-spec-kit-nos-meus-projetos
tags:
  - ia
  - spec-driven-development
  - spec-kit
  - engenharia-de-software
  - desenvolvimento
draft: false
description: "Um passo a passo prático de como eu tenho usado Spec-Driven Development com o Spec Kit para parar de pedir coisa solta para agente e começar a trabalhar com mais clareza e menos improviso."
---

# Como eu tenho usado Spec-Driven Development com o Spec Kit nos meus projetos

Se você já tentou construir software com agente de código, provavelmente já passou por essa montanha-russa. Tem dia que a coisa anda bem demais. Em outro, o agente entrega metade do que você pediu, inventa uma estrutura nada a ver, quebra a build ou até faz algo que parece funcionar, mas com uma base que você mesmo não faria daquele jeito.

Eu venho pensando bastante sobre isso. E, para mim, o problema quase nunca está só no modelo. Na maior parte das vezes, o problema está no jeito que a gente pede. Pedido solto gera resposta solta. Contexto mal amarrado gera decisão torta. E, quando não existe um jeito claro de dizer o que precisa ser construído e como aquilo vai ser validado, a chance de virar improviso é grande demais.

Foi por isso que comecei a olhar com mais atenção para **Spec-Driven Development**, ou simplesmente **SDD**. E, dentro disso, uma ferramenta que me chamou atenção foi o **Spec Kit**, um toolkit open source criado justamente para organizar esse fluxo de trabalho com agentes.

Neste texto, eu quero te mostrar como eu tenho enxergado esse processo na prática. Não como papo bonito, mas como um jeito mais sério de trabalhar com IA no desenvolvimento. A ideia aqui é sair do prompt jogado no chat e entrar em um fluxo com princípios, especificação, plano, tarefas e implementação.

## O que me incomoda no tal do vibe coding

Tem um jeito de usar IA para programar que funciona muito bem para protótipo rápido. Você abre o chat, manda algo como "cria uma tela de login" e vai refinando no teste e erro. Isso tem seu valor. Eu mesmo faço isso em alguns momentos.

O problema é quando essa mesma lógica vai parar em projeto real.

Quando o projeto precisa durar mais que uma tarde, quando existe manutenção, quando existe padrão, quando existe arquitetura, quando existe responsabilidade técnica, esse modelo começa a fazer barulho. Porque o agente até reconhece padrão muito bem, mas ele não adivinha intenção. Ele precisa de direção.

Foi aí que o SDD começou a fazer sentido para mim. A proposta é simples: em vez de começar direto no código, eu começo pela intenção. Eu defino princípios do projeto, descrevo o que quero construir, organizo as decisões técnicas e só depois parto para execução. O código continua importante, claro, mas deixa de ser a primeira coisa da conversa.

## O que é o Spec Kit

Na definição do próprio projeto, o **Spec Kit** é um toolkit open source voltado para te ajudar a focar em cenários de produto e resultados previsíveis, em vez de sair codando tudo na doidice.

A ideia central do toolkit conversa muito com o que eu venho buscando na prática: transformar especificação em parte ativa do desenvolvimento, e não em documento morto que só existe para cumprir tabela.

O fluxo principal dele gira em torno de cinco etapas:

1. `constitution`
2. `specify`
3. `plan`
4. `tasks`
5. `implement`

Parece simples, e de fato é. O valor não está em inventar moda. Está em botar ordem na casa.

## Antes de tudo: o que eu gosto nessa abordagem

O que mais me atrai aqui não é "automatizar tudo". É justamente o contrário. É criar um processo em que eu continuo segurando a direção.

Quando eu uso esse fluxo, eu não estou terceirizando pensamento. Estou botando ordem no pensamento. A IA entra como parceira de elaboração, refinamento e execução, mas a responsabilidade pela qualidade continua sendo minha.

Esse ponto é importante porque muita gente olha para ferramentas assim e imagina que o ganho está em apertar um botão e sair um sistema pronto. Eu não vejo desse jeito. Para mim, o ganho está em diminuir ruído e mal-entendido.

## Pré-requisitos

Para usar o Spec Kit, você precisa ter algumas coisas no ambiente:

- `uv` para gerenciar a instalação da CLI
- `Python 3.11+`
- `Git`
- Um agente compatível

O projeto suporta vários agentes. Entre eles, **GitHub Copilot**, **Claude Code**, **Codex CLI**, **Cursor**, **Gemini CLI** e outros.


## Instalando a CLI

A forma recomendada pelo projeto é instalar a CLI com `uv tool install`.

Exemplo:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
```

Se você quiser usar a versão mais recente da branch principal:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Depois disso, você já pode usar comandos como:

```bash
specify init <PROJECT_NAME>
specify check
```

Se a ideia for rodar sem instalar de forma persistente, também dá para usar `uvx`.

## Criando um projeto com o Spec Kit

Depois da instalação, eu inicializo o projeto com `specify init`.

Exemplo para criar um novo projeto:

```bash
specify init meu-projeto --ai copilot
```

Se eu quiser usar no diretório atual:

```bash
specify init . --ai copilot
```

No caso do **Codex CLI**, eu usaria algo assim:

```bash
specify init . --ai codex --ai-skills
```

Se eu fosse fazer a mesma coisa com **Claude Code**, seria assim:

```bash
specify init . --ai claude
```

Esse detalhe do `--ai-skills` importa porque, no Codex, o Spec Kit funciona como skill em vez de slash command tradicional.

Depois do `init`, o toolkit monta a base da estrutura do projeto. Entre os arquivos e pastas, normalmente você vai ver coisas como:

- `.specify/memory/constitution.md`
- `.specify/templates/`
- `.specify/scripts/`
- `.specify/specs/<feature>/`

Além disso, ele instala os comandos que vão guiar o processo.

Depois que essa base está pronta, você pode tocar esse fluxo do jeito que fizer mais sentido no seu dia a dia: no chat da sua IDE preferida, no agente via terminal ou na ferramenta que você estiver usando.

## Etapa 1: definindo os princípios com `constitution`

Essa é uma parte que eu acho boa mesmo. Antes de falar da feature, eu defino os princípios que vão mandar no projeto.

No fluxo tradicional do Spec Kit, o comando é:

```bash
/speckit.constitution
```

No Codex com skills, ficaria equivalente a:

```bash
$speckit-constitution
```

Aqui eu não descrevo tela nem endpoint. Eu descrevo regra de qualidade e critério de decisão.

Dependendo do contexto, essa etapa também pode registrar regras operacionais e requisitos transversais do projeto, como política de testes, fluxo de branch e exigências mínimas de segurança. Se isso muda a forma como o trabalho deve ser construído e revisado, faz sentido declarar já na `constitution`.

Por exemplo:

```text
Crie princípios focados em clean code. O projeto deve ser pequeno e simples. Não deve ter testes automatizados nesta primeira versão.
```

O resultado disso vai para o arquivo de constituição do projeto. E o que eu gosto é que isso puxa as próximas etapas. O agente passa a carregar esses princípios como referência.

Isso ajuda a evitar uma coisa que me incomoda bastante: o agente começar a inventar moda em um projeto simples.

## Etapa 2: descrevendo o que eu quero construir com `specify`

Depois dos princípios, eu parto para a especificação funcional.

Aqui o foco é no **o que** e no **porquê**, não na stack. Essa separação faz diferença. Se eu misturo requisito funcional com detalhe técnico cedo demais, eu mesmo embanano a conversa.

Exemplo de comando:

```bash
/speckit.specify
```

Ou no Codex:

```bash
$speckit-specify
```

E aí eu passo algo nessa linha:

```text
Construa uma aplicação que me ajude a gerenciar minhas tarefas e acompanhar atividades do dia a dia. As tarefas devem ter título, descrição, data de conclusão, prioridade e status. Inclua filtros para visualizar tarefas por prioridade, status ou data.
```

A partir disso, o Spec Kit gera uma especificação com histórias de usuário, requisitos e checklist de aceitação.

Essa é uma parte que eu recomendo revisar com calma. Não trate como final só porque o texto ficou arrumadinho. Leia de verdade. Veja se as histórias fazem sentido, se o escopo não saiu andando sozinho, se o checklist está coerente.

## Etapa 3: esclarecendo lacunas com `clarify`

Essa etapa é opcional no fluxo, mas eu diria que ela ajuda muito sempre que a especificação ficou vaga em algum ponto.

Comando:

```bash
/speckit.clarify
```

A função aqui é simples: identificar ponto mal definido antes do plano técnico. Isso evita retrabalho lá na frente.

Eu gosto dessa fase porque ela força uma conversa mais honesta com o problema. Às vezes a gente acha que sabe o que quer construir, mas descobre que ainda não decidiu nem coisa básica de comportamento.

Se a feature é pequena, talvez eu passe direto. Mas, se existir qualquer ambiguidade relevante, eu prefiro gastar energia aqui do que me lascar mais na frente, no meio da implementação.

## Etapa 4: criando o plano técnico com `plan`

Só aqui eu entro em stack, arquitetura e decisões técnicas.

Comando:

```bash
/speckit.plan
```

Ou:

```bash
$speckit-plan
```

Exemplo de prompt:

```text
A aplicação deve usar TypeScript, React Native com Expo para rodar no Expo Go, com o mínimo possível de bibliotecas e Expo Router para navegação. Armazene os dados em SQLite com Expo SQLite. Para esta versão, não inclua testes automatizados.
```

O que eu acho interessante nessa fase é que o toolkit não fica só em um resumão genérico. Ele tende a quebrar o plano em coisas mais concretas, como:

- `plan.md`
- `research.md`
- `data-model.md`
- contratos
- quickstart
- decisões de arquitetura

Se a stack escolhida muda rápido, essa é uma fase em que vale muito pesquisar versão, compatibilidade e detalhe específico. A própria documentação do Spec Kit sugere aprofundar a pesquisa quando a tecnologia for muito dinâmica.

## Etapa 5: quebrando o plano em tarefas com `tasks`

Depois do plano, eu gero a decomposição em tarefas.

Comando:

```bash
/speckit.tasks
```

Ou:

```bash
$speckit-tasks
```

Essa fase transforma o plano em uma lista executável. E isso é importante porque implementação boa não depende só de saber o que construir. Depende também de saber **em que ordem** construir.

O `tasks.md` costuma organizar o trabalho em fases, geralmente alinhadas com histórias de usuário, dependências técnicas e checkpoints.

Essa etapa me ajuda a enxergar se o plano está realmente implementável. Se a lista de tarefas sai esquisita, já é sinal de que o plano talvez ainda esteja mal resolvido.

## Etapa 6: implementando com `implement`

Com tudo pronto, aí sim eu peço para implementar.

Comando:

```bash
/speckit.implement
```

Ou:

```bash
$speckit-implement
```

Essa etapa pega o que foi definido antes e executa a implementação seguindo o que foi amarrado nas etapas anteriores.

É aqui que muita gente se empolga e acha que acabou o trabalho. Para mim, é justamente o contrário. É aqui que começa a parte mais importante: revisar o que foi feito com rigor e sem passar pano.

Porque uma implementação pode seguir o plano e ainda assim sair ruim. Pode sair com UX torta, estrutura desnecessária, abstração mal colocada ou pedaço pela metade.

Isso é um ótimo lembrete. O processo melhora muito a consistência, mas não elimina revisão humana.

## Um exemplo prático de fluxo

Se eu fosse resumir um fluxo real de uso, ficaria mais ou menos assim:

```bash
specify init . --ai codex --ai-skills
```

Depois, dentro do agente no **Codex**:

```text
$speckit-constitution
$speckit-specify
$speckit-clarify
$speckit-plan
$speckit-tasks
$speckit-implement
```

Se eu fosse fazer a mesma coisa no **Claude Code**, começaria assim:

```bash
specify init . --ai claude
```

Depois, dentro do agente:

```text
/speckit.constitution
/speckit.specify
/speckit.clarify
/speckit.plan
/speckit.tasks
/speckit.implement
```

## O que muda na prática quando eu trabalho assim

Para mim, a principal mudança é esta: eu paro de ficar negociando com resposta solta e começo a trabalhar com algo mais amarrado.

Em vez de ficar repetindo "não era isso", "faltou isso", "não gostei da estrutura", eu passo a ter etapas intermediárias onde consigo corrigir a rota com muito mais clareza:

- princípios
- especificação
- esclarecimentos
- plano técnico
- tarefas
- implementação

Isso reduz atrito e também reduz aquela sensação de que eu estou brigando com o agente o tempo inteiro.

## O que eu reviso em cada etapa

Eu não confio cegamente em nenhuma etapa. O que eu faço é revisar cada uma com um foco diferente:

### Na constituição

Eu olho se os princípios realmente refletem como quero que o projeto seja conduzido.

### Na especificação

Eu vejo se o problema foi descrito corretamente e se os requisitos não fugiram do escopo.

### Na clarificação

Eu procuro ponto nebuloso que ainda pode virar retrabalho.

### No plano

Eu avalio se a stack faz sentido, se não teve exagero e se as decisões técnicas estão coerentes com a constituição.

### Nas tarefas

Eu observo se a ordem de implementação está lógica e se não existe buraco óbvio no meio.

### Na implementação

Eu verifico comportamento real, estrutura, aderência aos princípios e acabamento técnico.

## Onde isso conversa com o jeito que a gente trabalha nas empresas

Uma coisa importante: eu não enxergo SDD como substituto direto de como os times já se organizam no dia a dia.

Na maior parte das empresas, a gente trabalha com algum formato de **Scrum**, **Kanban**, **Scrumban** ou alguma mistura própria que nasceu da realidade do time. Tem planning, refinamento, daily, review, card no board, prioridade mudando no meio da semana e aquele caos controlado que todo time conhece.

Para mim, o SDD entra em outra camada.

Ele não substitui backlog.
Ele não substitui sprint.
Ele não substitui board.
Ele não substitui alinhamento com produto.

O que ele faz é melhorar a qualidade da passagem entre intenção e implementação.

Em um time com **Scrum**, por exemplo, eu consigo imaginar muito bem uma história entrando na sprint e sendo detalhada com esse fluxo de constituição, especificação, plano e tarefas antes da implementação pesada começar.

Em um time mais puxado para **Kanban**, isso também faz sentido, porque dá para usar o SDD como forma de deixar cada item que entra em execução menos nebuloso e menos dependente de interpretação solta no chat.

E no caso do **Scrumban**, que é a realidade de muito lugar, isso encaixa talvez até melhor, porque você consegue manter cadência, prioridade e fluxo contínuo sem abrir mão de especificar melhor o que está sendo feito.

Então, pelo menos hoje, eu vejo SDD muito mais como complemento de processo do que como substituição de processo. Ele senta bem do lado das práticas que a maioria dos times já usa. A diferença é que agora existe um jeito mais forte de estruturar a conversa entre requisito, decisão técnica e execução com agente.

Para ficar mais concreto, imagina uma task comum de empresa.

O card chega mais ou menos assim:

```text
Adicionar filtro de status na listagem de pedidos do painel administrativo.
O usuário precisa conseguir visualizar pedidos por status: pendente, pago, enviado e cancelado.
```

Na vida real, muitas vezes isso entra no board desse jeito mesmo. Talvez venha com um comentário do produto, talvez venha com um print do Figma, talvez venha com meia dúzia de mensagens no Slack ou no Jira explicando por cima. Aí o dev pega isso, interpreta do seu jeito, abre o projeto e começa a implementar.

É justamente aí que muita coisa desanda.

Porque começam a aparecer perguntas que ninguém respondeu direito:

- esse filtro pode ser combinado com busca por texto?
- o status vem do backend ou vai ser mapeado no frontend?
- o filtro precisa ficar persistido na URL?
- quando não houver resultado, qual estado a tela mostra?
- isso precisa alterar paginação?
- existe impacto em performance ou índice no banco?

Sem um processo melhor, essas respostas ficam espalhadas em comentário de card, conversa de daily, mensagem no chat e decisão tomada no susto durante a implementação.

---

Ta gostando do artigo? 


Se esse tipo de conteúdo faz sentido para você, dá uma olhada no meu canal no YouTube:

[youtube.com/@o.raphadev](https://www.youtube.com/@o.raphadev)

Por lá eu falo sobre engenharia de software, IA aplicada ao desenvolvimento, arquitetura, carreira e essas mudanças que estão mexendo com o nosso jeito de construir software.

E, se você trabalha com produto SaaS e segurança é uma preocupação real no teu contexto, também vale conhecer a **BetaCoding**:

[betacoding.com.br](https://betacoding.com.br)

Na BetaCoding, a gente atua com foco em **cybersegurança para SaaS**, olhando para a proteção do produto de um jeito mais próximo da realidade de quem constrói e mantém software de verdade.

---

É nesse ponto que eu vejo o SDD entrando.

Em vez de sair codando em cima do card cru, eu posso pegar essa task e passar por um fluxo mais organizado:

1. Na `specify`, eu transformo o pedido solto em uma descrição mais clara do comportamento esperado.
2. Na `clarify`, eu levanto as dúvidas que ainda estão em aberto.
3. Na `plan`, eu defino como isso entra na stack atual do projeto.
4. Na `tasks`, eu quebro isso em passos menores e implementáveis.
5. Na `implement`, aí sim eu executo.

Se eu fosse fazer isso na prática, poderia ficar algo assim.

### Exemplo de task no fluxo atual

```text
Task: adicionar filtro de status na listagem de pedidos do admin.

Critério de aceite:
- filtrar por pendente, pago, enviado e cancelado
- permitir limpar filtro
- manter layout atual da listagem
```

### A mesma task entrando no SDD

Na etapa de `specify`, eu escreveria algo nessa linha:

```text
Adicionar à tela de listagem de pedidos do painel administrativo a capacidade de filtrar pedidos por status. O usuário deve conseguir visualizar pedidos pendentes, pagos, enviados e cancelados, além de remover o filtro e voltar a ver todos os pedidos. O objetivo é facilitar a operação do time administrativo sem alterar o layout principal da listagem.
```

Na etapa de `clarify`, eu provavelmente levantaria perguntas como:

- esse filtro pode ser combinado com a busca já existente?
- o filtro precisa sobreviver ao refresh da página?
- o backend já suporta esse parâmetro ou vai precisar de ajuste?
- qual deve ser o comportamento quando nenhum pedido for encontrado?

Na etapa de `plan`, eu descreveria algo mais técnico, por exemplo:

```text
Implementar o filtro de status reaproveitando a listagem atual de pedidos no admin. No frontend, adicionar um seletor simples acima da tabela. Persistir o filtro na query string para permitir compartilhamento de URL e manter estado após refresh. No backend, aceitar o parâmetro status no endpoint de listagem, validando apenas os valores permitidos. Não alterar o contrato de resposta da API além do suporte ao novo parâmetro de entrada.
```

Depois disso, na etapa de `tasks`, a decomposição poderia sair mais ou menos assim:

```text
1. Atualizar a especificação da listagem de pedidos com o novo comportamento de filtro por status
2. Ajustar o endpoint de listagem para aceitar o parâmetro status
3. Validar os valores permitidos no backend
4. Atualizar a consulta ao banco para filtrar por status
5. Adicionar o seletor de status na interface do admin
6. Sincronizar o filtro com a query string
7. Exibir estado vazio quando nenhum pedido corresponder ao filtro
8. Validar manualmente os quatro status e a limpeza do filtro
```

Olha a diferença: a task continua sendo a mesma, mas agora ela deixa de ser só um card solto no board e passa a ter intenção, dúvida explícita, decisão técnica e caminho de implementação.

É esse tipo de coisa que me faz olhar para SDD com interesse real dentro de empresa. Não porque ele vai matar Scrum, Kanban ou qualquer outra prática, mas porque ele ajuda a reduzir aquele buraco entre "o card chegou" e "alguém começou a codar".

## Onde eu acho que o Spec Kit realmente ajuda

Tem três pontos em que eu vejo valor bem claro.

O primeiro é **coerência**. Como cada etapa herda contexto da anterior, o agente tende a manter uma linha mais estável de decisão.

O segundo é **rastro de decisão**. Fica mais fácil entender de onde saiu uma escolha, porque ela geralmente está ancorada em alguma etapa anterior.

O terceiro é **menos bagunça**. Não no sentido de que tudo vai sair perfeito, mas no sentido de que o processo deixa menos espaço para improviso puro.

## Onde eu acho que você precisa tomar cuidado

Também não acho que essa abordagem seja mágica. Tem alguns cuidados importantes.

### 1. Pode parecer burocrático em projeto pequeno

Se a feature é minúscula, esse fluxo inteiro talvez pareça pesado demais. E às vezes é mesmo. Nem tudo precisa virar cerimônia.

### 2. Especificar bem é difícil

Escrever boa especificação não é simples. Separar intenção funcional de decisão técnica exige prática. No começo, é normal misturar as coisas.

### 3. O agente ainda pode exagerar

Mesmo com todo o processo, ainda existe risco de overengineering. O plano pode vir mais complexo do que o necessário. A implementação pode trazer coisa que você não pediu.

### 4. Implementado não significa resolvido

Se o agente marcou tarefa como concluída, isso não quer dizer que a experiência final ficou boa ou que todos os requisitos foram realmente entregues.

## O que eu aprendi até aqui

Se eu tivesse que resumir minha leitura prática do SDD com o Spec Kit, seria esta: **a qualidade da especificação virou uma parte muito mais central do trabalho de desenvolvimento com IA**.

Isso não diminui o papel do programador. Pelo contrário. Exige mais maturidade.

Eu preciso entender melhor de produto para descrever intenção.
Eu preciso entender melhor de arquitetura para escolher direção técnica.
Eu preciso entender melhor de qualidade para revisar o que foi produzido.
Eu preciso entender melhor de escopo para não deixar a ferramenta sair correndo sozinha.

No fim, usar IA desse jeito não me transforma em alguém menos técnico. Só muda o lugar onde o rigor aparece.

## Se você quiser começar sem complicar

Se eu fosse te sugerir um caminho simples para testar isso no seu próximo projeto, eu faria assim:

1. Escolha uma feature pequena, mas real.
2. Defina princípios curtos e objetivos.
3. Descreva o que quer construir sem falar de stack.
4. Esclareça lacunas antes de planejar.
5. Só depois dê as decisões técnicas.
6. Revise tarefas antes da implementação.
7. Trate a implementação como rascunho sério, não como verdade final.

Esse fluxo já é suficiente para você sentir a diferença entre pedir "faz aí" e conduzir o agente com método.

## Fechando

Eu ainda estou aprendendo a usar esse tipo de abordagem no meu dia a dia. Não acho que o SDD vá substituir todo e qualquer fluxo, nem que o Spec Kit seja a única ferramenta possível para isso. Mas eu realmente acho que tem um negócio importante aqui.

Quando eu especifico melhor, o agente trabalha melhor.
Quando eu estruturo o processo, a revisão fica melhor.
Quando eu saio do improviso, o código tende a sair menos torto.

E, para mim, esse é o ponto.

Não se trata de terceirizar o desenvolvimento para a IA.
Se trata de criar um processo em que eu continuo pensando como engenheiro, mas usando a IA para ganhar braço sem soltar o juízo.

## Série de aprofundamento

Se você quiser acompanhar os textos em que eu aprofundo cada etapa separadamente, esta é a sequência:

- [No Spec-Driven Development, tudo começa pelos princípios](/2026/04/06/no-spec-driven-development-tudo-comeca-pelos-principios/)    
  Lançamento: 06 de abril de 2026
  
- [No Spec-Driven Development, `specify` é onde a ambiguidade começa a morrer](/2026/04/13/no-spec-driven-development-specify-e-onde-a-ambiguidade-comeca-a-morrer/)  
  Lançamento: 13 de abril de 2026

- [No Spec-Driven Development, `plan` é onde a especificação vira estratégia de execução](/2026/04/20/no-spec-driven-development-plan-e-onde-a-especificacao-vira-estrategia-de-execucao/)  
  Lançamento: 20 de abril de 2026

- [No Spec-Driven Development, `tasks` é onde o plano vira unidades concretas de trabalho](/2026/04/27/no-spec-driven-development-tasks-e-onde-o-plano-vira-unidades-concretas-de-trabalho/)  
  Lançamento: 27 de abril de 2026

- [No Spec-Driven Development, `implement` é onde todo o resto vira código](/2026/05/04/no-spec-driven-development-implement-e-onde-todo-o-resto-vira-codigo/)  
  Lançamento: 04 de maio de 2026
