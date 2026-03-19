---
title: "Ensinando o Copilot a falar a linguagem do seu repositório"
date: '2025-10-29T14:46:13-03:00'
slug: ensinando-o-copilot-a-falar-a-linguagem-do-seu-repositorio
draft: false
description: "Trabalhando há mais de 14 anos com desenvolvimento de software, sempre me pego pensando sobre as tendências e novidades das tecnologias que podem ser usadas..."
---

Trabalhando há mais de 14 anos com desenvolvimento de software, sempre me pego pensando sobre as tendências e novidades das tecnologias que podem ser usadas para **reduzir atrito no dia a dia do dev**.

Vocês sabiam que existe a possibilidade de adicionar **instruções personalizadas diretamente no seu repositório para agentes de IA?**Basicamente, você pode “ensinar” o Copilot sobre as regras, padrões e estilos do seu projeto, e ele vai gerar sugestões muito mais alinhadas ao que você e sua equipe realmente precisam.

É como ter um colega de trabalho que já leu toda a documentação do projeto e sabe exatamente o que deve ou não sugerir e esse colega não dorme, não cansa e ainda está sempre pronto pra te ajudar a codar.

Esse recurso é um passo incrível para transformar o Copilot em algo mais do que apenas um “autocomplete inteligente”: ele vira um **membro ativo da equipe**, moldado pelo contexto que você mesmo fornece.

![](https://cdn-images-1.medium.com/max/1024/1*pRpE_OerwUnYxytxY7PPQg.png)

_[Imagem gerada por IA]_

### Visão Geral

Aqui vamos nos basear no Copilot, pois ele tem a **possibilidade de dar contexto ao repositório**. Em vez de apenas gerar código “genérico”, agora conseguimos **ensinar a IA sobre as regras do projeto**, convenções, frameworks e até os pequenos detalhes que normalmente só quem já está no time conhece.

Na prática, isso transforma o Copilot em algo muito além de um autocomplete inteligente: ele passa a ser um **parceiro técnico moldado pelo seu repositório**. Se você trabalha em um projeto grande, com múltiplos módulos e stacks diferentes, ter instruções personalizadas é como escrever um manual para a IA.

E o melhor: tudo isso fica versionado no próprio repositório. Ou seja, qualquer dev que clonar o projeto já herda o mesmo nível de contexto.

![](https://cdn-images-1.medium.com/max/1024/1*tZig2YF4TxvYyWS_hgo6eg.png)

_[Imagem gerada por IA]_

### Pré-requisitos

Antes de sair configurando, vale checar alguns pontos básicos:

**1. Arquivo de instruções no repositório**

- Crie o .github/copilot-instructions.md na raiz do projeto (ou arquivos específicos em .github/instructions/).
- Esse é o “manual” que o Copilot vai ler para se alinhar às práticas da sua equipe.

**2. Funcionalidade habilitada**

- O recurso ainda está em *public preview*, então precisa estar ativo na sua conta/organização.

**3. IDE/Editor atualizado**

- Certifique-se de estar usando a versão mais recente do GitHub Copilot no VS Code, JetBrains ou na interface web, porque só essas versões já entendem instruções customizadas.

**4. Consciência de contexto**

- As instruções são aplicadas em conjunto com outras camadas (pessoais, de organização, etc.). Ou seja, evite contradições: se no repositório você diz “use React”, mas nas instruções pessoais pede “prefira Vue”, o Copilot pode se perder.

Com isso pronto, você já está no ponto de começar a personalizar sua experiência com o Copilot e moldar as sugestões de código ao seu estilo e às necessidades reais do projeto.

![](https://cdn-images-1.medium.com/max/1024/1*afncu7piYCLhP9MVsPy1LQ.png)

_[Imagem gerada por IA]_

### Tipos de Instruções Personalizadas

Esse é o ponto em que o Copilot deixa de ser “só um assistente genérico” e realmente começa a **falar a língua do seu projeto**. Existem três formas principais de você dar instruções, e cada uma tem sua utilidade dependendo do tamanho e da complexidade do repositório.

#### 1. Instruções de Repositório (repository-wide)

Aqui é onde você define as **regras gerais do jogo**.
Um arquivo chamado .github/copilot-instructions.md fica na raiz e serve como guia para tudo que acontece dentro do repositório. É nele que você pode escrever coisas como:

- “Prefira **TypeScript** a JavaScript.”
- “Use **arquitetura limpa** no backend.”
- “Os testes devem ser escritos com **JUnit**.”

Na prática, é como se você tivesse um README secreto só para o Copilot.

![](https://cdn-images-1.medium.com/max/1024/1*IIPHbY7OjE-xGpcoBlVprQ.png)

_[Imagem gerada por IA]_

#### 2. Instruções Específicas de Caminho (path-specific)

Agora imagine um projeto monolito com várias áreas: API, front, mobile, scripts de infra. Cada uma pode ter **regras diferentes**.
Com instruções específicas, você cria arquivos dentro de .github/instructions/ e usa padrões glob (applyTo) para dizer onde elas se aplicam.

Exemplo prático:

```text
---
applyTo: "src/**/*.ts"
---
Sempre use async/await em vez de Promises encadeadas.
```

Isso é poderoso porque evita que o Copilot sugira código fora do padrão em partes específicas do projeto.

![](https://cdn-images-1.medium.com/max/1024/1*_5yNfP4KwwhEaeyOWzd92g.png)

_[Imagem gerada por IA]_

### Uso em Ambiente Real e Verificações

Depois que você cria os arquivos de instruções, o Copilot começa a agir como se tivesse lido toda a documentação do projeto. **E sim, dá pra verificar se isso está rolando de verdade**.

#### Como funciona na prática

- A cada sugestão, o Copilot “lê” as instruções junto com o código.
- Se você está num arquivo que bate com um applyTo, as instruções específicas são aplicadas junto com as gerais.
- Isso permite que seja retornado sugestões mais próximas do estilo e padrões que você definiu.

É como se fosse um *linter vivo* que, em vez de só apontar erros, já sugere o código certo de primeira.

#### Como verificar se está funcionando

Dentro do **Copilot Chat** (na IDE ou no GitHub), muitas vezes dá pra ver a seção de **Referências** no final da resposta da IA.

- Se aparecer algo como .github/copilot-instructions.md, é sinal de que o Copilot usou suas instruções.
- Se não aparecer, pode ser que o arquivo não esteja configurado no lugar certo ou que não esteja habilitado no chat.

É um detalhe simples, mas que ajuda a ter certeza de que o esforço de configurar não foi em vão.

#### Atenção para conflitos

Vale lembrar que o Copilot também leva em conta:

- **Instruções pessoais do dev** (o que você configurou na sua conta).
- **Instruções da organização**.
- **Instruções do repositório**.

Se elas entrarem em conflito (“use Vue” vs “use React”), o comportamento pode ficar imprevisível. Por isso, é bom alinhar com o time e evitar contradições.

![](https://cdn-images-1.medium.com/max/1024/1*whdd7P_BMqNQPFHOH5eY9Q.png)

_[Imagem gerada por IA]_

### Habilitar ou Desabilitar

Nem sempre você vai querer que o Copilot siga as instruções do repositório. Às vezes, você quer que ele pense “fora da caixa” ou que ignore regras específicas só pra experimentar uma abordagem nova. E sim, dá pra **ligar e desligar as instruções personalizadas** de forma simples.

#### No Copilot Chat

Se você estiver dentro do repositório, o chat mostra um botãozinho para **“Enable/Disable custom instructions”**. É basicamente um switch:

- Ativado → o Copilot lê o .github/copilot-instructions.md e os arquivos dentro de .github/instructions/.
- Desativado → ele ignora essas regras e gera código como se fosse um autocomplete normal.

É útil quando você quer testar soluções alternativas sem o filtro das regras do time.

#### Na Revisão de Código (Pull Requests)

No próprio GitHub, você pode configurar se o Copilot deve ou não considerar as instruções personalizadas ao revisar PRs.

O caminho é: **Settings → Code & automation → Copilot → Code review → Use custom instructions when reviewing pull requests**.

Se desligar essa opção, o Copilot revisa o PR sem olhar para as regras do repositório.

### Recomendações Práticas (na visão de um desenvolvedor experiente)

Depois de anos lidando com projetos mobile, web e backends, aprendi que a diferença entre uma equipe que “usa uma ferramenta” e uma equipe que **extrai valor real dela** está nas pequenas práticas do dia a dia. Aqui vão algumas dicas que eu aplicaria sem pensar duas vezes ao trabalhar com instruções personalizadas no Copilot:

#### 1. Documente para humanos, não só para a IA

Não caia na tentação de escrever instruções pensando só no Copilot. Escreva como se estivesse explicando para um novo colega que acabou de entrar no time. Isso garante clareza tanto para pessoas quanto para a IA.

👉 Exemplo:
**“Prefira async/await ao invés de then/catch” é muito mais útil do que “use async/await”.**

#### 2. Evite contradições entre instruções

Já vi times se enrolarem porque no repo dizia “use React” e nas instruções pessoais de cada dev estava “prefira Vue”.

Defina **uma fonte de verdade** e mantenha alinhado com todos.

#### 3. Atualize conforme o projeto evolui

Seu projeto não é estático. Hoje pode ser Flutter 3.22, amanhã pode estar em 3.27. Se você não atualizar as instruções, vai receber sugestões desatualizadas que só dão retrabalho. Reserve momentos (ex.: fim de sprint) para revisar o copilot-instructions.md.

#### 4. Inclua convenções de código e arquitetura

Defina como o time quer que o código seja escrito.

- Nome de variáveis (camelCase, snake_case).
- Padrão de commits.
- Frameworks e libs preferenciais.
- Estrutura de camadas (ex.: “Controllers nunca chamam DB direto”).

Isso faz o Copilot sugerir código **já no formato que passa no code review**.

#### 5. Use como ferramenta de onboarding

Novos devs sempre sofrem no começo pra entender o “jeito do time”. Se o Copilot já sugere código alinhado ao padrão, o onboarding fica muito mais rápido e suave.

#### 6. Teste o impacto

Não confie só na sensação de que “melhorou”. Compare PRs de antes e depois das instruções: menos comentários sobre estilo? Menos erros de build? Se sim, você está no caminho certo.

Então, se tem uma coisa que aprendi nesses 14 anos de estrada é que tecnologia não é só sobre código, é sobre **como a gente usa as ferramentas pra trabalhar melhor, em equipe, e criar soluções que fazem diferença**.

O GitHub Copilot com instruções personalizadas é justamente isso: um passo além do autocomplete. É como pegar toda a cultura, padrões e experiência do seu time e colocar ao lado da IA, transformando ela num verdadeiro parceiro de desenvolvimento.

E aí, a bola está contigo:

- Vai deixar o Copilot ser apenas mais uma ferramenta na sua stack?
- Ou vai ensinar ele a jogar o jogo do seu time, falando a mesma língua que você?

Minha dica: **experimenta no seu próximo projeto**. Começa simples, escreve duas ou três instruções que já fazem diferença no dia a dia e sente o impacto. Tenho certeza que, assim como aconteceu comigo, você vai perceber que está colocando o Copilot não só como assistente, mas como parte viva da sua equipe. 🚀

![](https://cdn-images-1.medium.com/max/1024/1*lsVfvfCIuuQCIaCXgL_m6Q.png)

_[Imagem gerada por IA]_

Sou desenvolvedor há mais de 14 anos, pós-graduado em Engenharia de Software e Desenvolvimento Mobile, e escrevo para compartilhar aprendizados reais de quem está na trincheira da tecnologia todos os dias.

**Leia mais artigos meus em:** [medium.com/@raphaelkennedy](https://medium.com/@raphaelkennedy)

[[ [Buy me a coffee](http://buymeacoffee.com/raphaelpontes) ]]

**Siga-me nas redes**

- Linkedin: [raphaelkennedy](https://www.linkedin.com/in/raphaelkennedy)
- Youtube: [@raphaelpontes](https://youtube.com/@raphaelpontes)
