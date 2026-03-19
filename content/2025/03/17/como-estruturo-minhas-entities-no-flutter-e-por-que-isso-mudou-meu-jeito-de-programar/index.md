---
title: "Como estruturo minhas Entities no Flutter e por que isso mudou meu jeito de programar"
date: '2025-03-17T18:22:49-03:00'
slug: como-estruturo-minhas-entities-no-flutter-e-por-que-isso-mudou-meu-jeito-de-programar
draft: false
description: "Fala, dev! Se você já precisou consumir múltiplas APIs em um app Flutter, sabe que a bagunça pode começar rápido. No começo, parece simples: você pega os dad..."
---

Fala, dev!

Se você já precisou consumir múltiplas APIs em um app Flutter, sabe que a bagunça pode começar rápido. No começo, parece simples: você pega os dados da API, joga direto no modelo e pronto! Mas aí vem aquele momento em que precisa integrar uma segunda API, lidar com mudanças inesperadas no backend ou até mesmo otimizar o carregamento dos dados. E de repente… BOOM💥! Seu código vira um verdadeiro Frankenstein, difícil de entender e ainda mais difícil de manter.

Foi exatamente isso que aconteceu comigo no início da minha jornada. Até que eu descobri a importância de **Entities**, **Adapters** e **DTOs**. Essas três camadas mudaram minha forma de programar e deixaram meus apps mais organizados e fáceis de escalar.

Hoje quero te contar como estruturo tudo isso e por que essa abordagem pode salvar seu código também.

![](https://cdn-images-1.medium.com/max/480/0*nedp-VQ57p-PWpNJ.gif)

### O que é uma Entity e por que você deveria usá-la?

A **Entity** (ou Entidade) é o coração do seu modelo de dados. Ela representa o conceito puro e independente dos dados dentro do seu domínio de aplicação, sem se preocupar com detalhes de infraestrutura como API, banco de dados ou arquivos locais.

A principal vantagem de ter uma Entity bem definida é que ela mantém seu código desacoplado. Isso significa que, independentemente de onde os dados venham (API, SQLite, Firebase, etc.), sua lógica de negócio sempre trabalhará com a mesma estrutura.

Vamos a um exemplo. Imagine que seu app trabalha com usuários e recebe da API um JSON assim:

```text
{
  "id_usuario": 123,
  "nome_completo": "João Silva",
  "email": "joao@email.com",
  "idade": 30
}
```

Se você usar esse formato diretamente no app, qualquer mudança no backend pode quebrar seu código. Mas se você definir uma **Entity**, seu modelo interno ficará estável:

```text
class User {
  final int id;
  final String name;
  final String email;
  final int age;
  
  User({
    required this.id,
    required this.name,
    required this.email,
    required this.age,
  });
}
```

Agora, o resto do app só precisa conhecer essa entidade **User**, sem se preocupar com como os dados chegam ou são armazenados. Se amanhã a API mudar id_usuario para userId, o app continua funcionando perfeitamente—desde que a conversão seja tratada no lugar certo.

E é aí que entra o **Adapter**.

### O que é um Adapter e por que ele é essencial?

O **Adapter** é o responsável por traduzir os dados externos (API, banco de dados, cache) para o formato interno do app e vice-versa. Ele permite que sua **Entity** continue limpa e independente de qualquer fonte de dados externa.

### Exemplo de Adapter

Aqui está um Adapter que converte o JSON da API para a nossa **Entity User**:

```text
class UserAdapter {
  static User fromJson(Map<String, dynamic> json) {
    return User(
      id: json['id_usuario'],
      name: json['nome_completo'],
      email: json['email'],
      age: json['idade'],
    );
  }
  
  static Map<String, dynamic> toJson(User user) {
    return {
      'id_usuario': user.id,
      'nome_completo': user.name,
      'email': user.email,
      'idade': user.age,
    };
  }
}
```

Agora, se o backend decidir mudar os nomes dos campos, eu só preciso alterar esse Adapter e pronto! O resto do app continua funcionando perfeitamente, pois ele sempre lida apenas com a entidade **User**.

O Adapter evita que o app precise conhecer detalhes específicos de diferentes APIs. Se você precisar consumir múltiplas fontes de dados com formatos distintos, cada uma pode ter seu próprio Adapter sem impactar a lógica do seu app.

### O que é um DTO e por que ele é diferente do Adapter?

Enquanto o Adapter serve para converter dados de uma API para uma **Entity**, o **DTO (Data Transfer Object)** é usado para definir exatamente quais dados serão transportados entre camadas do sistema.

A diferença é que um DTO não precisa ter a mesma estrutura da Entity. Ele pode ser um subconjunto dos dados ou até conter informações formatadas de maneira diferente.

### Exemplo de DTO

Digamos que precisamos enviar um usuário para a API, mas a entidade **User** contém informações que não precisam ser transmitidas, como um campo createdAt.

Em vez de enviar a **Entity** inteira, criamos um DTO para definir exatamente o que será enviado:

```text
class UserDTO {
  final String name;
  final String email;
  final int age;

  UserDTO({
    required this.name,
    required this.email,
    required this.age,
  });
  
  Map<String, dynamic> toJson() {
    return {
      'nome_completo': name,
      'email': email,
      'idade': age,
    };
  }
  
  factory UserDTO.fromJson(Map<String, dynamic> json) {
    return UserDTO(
      name: json['nome_completo'],
      email: json['email'],
      age: json['idade'],
    );
  }
}
```

Aqui, o DTO serve como um modelo intermediário para garantir que só os dados necessários sejam transmitidos. Isso melhora a performance da comunicação e evita vazamento de informações desnecessárias.

### Resumo da Ópera

**Entity** Representa os dados puros e internos do domínio do app SEMPRE, para garantir que o código esteja desacoplado da API ou banco de dados.

**Adapter** Converte dados entre a API e a Entity quando a estrutura da API é diferente da estrutura interna do app.

**DTO** define um modelo específico para transportar dados entre camadas do sistema quando há necessidade de transmitir apenas parte dos dados ou formatá-los de forma específica.

Bom, estamos quase concluindo nosso artigo, mas eu sei que você leitor me perguntou mentalmente assim:

E a resposta é simples… **Sim, podemos**. Irei explicar isso no próximo tópico.

### Quando usar Adapter e DTO juntos?

Em alguns casos, podemos combinar os dois. Veja um fluxo comum:

1. A API retorna dados → O **Adapter** transforma a resposta da API em uma **Entity**.
2. O app precisa enviar dados para a API → Criamos um **DTO** para representar exatamente o que será enviado.
3. O DTO pode ser passado para o Adapter, que então faz a conversão necessária antes de enviar os dados para a API.

Isso garante um código bem estruturado, fácil de testar e manter.

![](https://cdn-images-1.medium.com/max/499/0*vhpb7CdMOGg_wBFx.gif)

### Conclusão

Se tem algo que aprendi programando no Flutter (e apanhando com APIs diferentes), é que separar bem as responsabilidades do código faz toda a diferença.

- **Entities** deixam o código limpo e independente da API.
- **Adapters** protegem o app de mudanças inesperadas no backend.
- **DTOs** garantem que apenas os dados necessários sejam transportados.

No fim das contas, tudo isso faz com que seu código fique mais organizado, escalável e fácil de testar.

Se você ainda não estruturou seu código assim, experimenta! Tenho certeza de que, depois que começar, nunca mais vai querer voltar atrás.

E você, já usa essa abordagem? Como estrutura suas entidades no Flutter? Vamos trocar ideia aqui ou nas minhas redes que deixei logo em baixo.

![](https://cdn-images-1.medium.com/max/480/0*SIS09iEdBEk4N9LF.gif)

Leia mais artigos meus: [medium.com/@raphaelkennedy](https://medium.com/@raphaelkennedy)

[[ [Buy me a coffee](http://buymeacoffee.com/raphaelpontes) ]]

Siga-me nas redes

- Linkedin: [raphaelkennedy](https://www.linkedin.com/in/raphaelkennedy)
- Youtube: [@raphaelpontes](https://youtube.com/@raphaelpontes)
