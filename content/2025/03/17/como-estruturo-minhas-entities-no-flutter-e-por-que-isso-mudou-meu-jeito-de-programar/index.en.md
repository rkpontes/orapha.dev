---
title: "How I Structure My Entities in Flutter and Why It Changed My Way of Programming"
date: '2025-03-17T18:22:49-03:00'
slug: como-estruturo-minhas-entities-no-flutter-e-por-que-isso-mudou-meu-jeito-de-programar
lang: en
translationKey: como-estruturo-minhas-entities-no-flutter-e-por-que-isso-mudou-meu-jeito-de-programar-2025-03-17
tags:
  - flutter
  - architecture
  - entities
  - clean-architecture
draft: false
description: "Hey dev! If you've ever needed to consume multiple APIs in a Flutter app, you know the mess can start quickly. At first, it seems simple..."
---

Hey dev!

If you've ever needed to consume multiple APIs in a Flutter app, you know the mess can start quickly. At first, it seems simple: you get the data from the API, throw it directly into the model, and done! But then comes that moment when you need to integrate a second API, deal with unexpected backend changes, or even optimize data loading. And suddenly... BOOM💥! Your code turns into a real Frankenstein, hard to understand and even harder to maintain.

That's exactly what happened to me at the beginning of my journey. Until I discovered the importance of **Entities**, **Adapters**, and **DTOs**. These three layers changed my way of programming and made my apps more organized and easier to scale.

Today I want to tell you how I structure all this and why this approach can save your code too.

![](https://cdn-images-1.medium.com/max/480/0*nedp-VQ57p-PWpNJ.gif)

### What is an Entity and why should you use it?

The **Entity** (or Entity) is the heart of your data model. It represents the pure and independent concept of data within your application domain, without worrying about infrastructure details like API, database, or local files.

The main advantage of having a well-defined Entity is that it keeps your code decoupled. This means that, regardless of where the data comes from (API, SQLite, Firebase, etc.), your business logic will always work with the same structure.

Let's look at an example. Imagine your app works with users and receives this JSON from the API:

```text
{
  "id_usuario": 123,
  "nome_completo": "John Silva",
  "email": "john@email.com",
  "idade": 30
}
```

If you use this format directly in the app, any change in the backend can break your code. But if you define an **Entity**, your internal model will remain stable:

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

Now, the rest of the app only needs to know this **User** entity, without worrying about how the data arrives or is stored. If tomorrow the API changes id_usuario to userId, the app continues to work perfectly—as long as the conversion is handled in the right place.

And that's where the **Adapter** comes in.

### What is an Adapter and why is it essential?

The **Adapter** is responsible for translating external data (API, database, cache) to the app's internal format and vice versa. It allows your **Entity** to remain clean and independent of any external data source.

### Adapter Example

Here is an Adapter that converts the API JSON to our **User Entity**:

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

Now, if the backend decides to change field names, I only need to change this Adapter and done! The rest of the app continues to work perfectly, as it only handles the **User** entity.

The Adapter prevents the app from needing to know specific details of different APIs. If you need to consume multiple data sources with different formats, each can have its own Adapter without impacting your app logic.

### What is a DTO and why is it different from Adapter?

While the Adapter serves to convert API data to an **Entity**, the **DTO (Data Transfer Object)** is used to define exactly which data will be transported between system layers.

The difference is that a DTO doesn't need to have the same structure as the Entity. It can be a subset of the data or even contain information formatted differently.

### DTO Example

Let's say we need to send a user to the API, but the **User** entity contains information that doesn't need to be transmitted, such as a createdAt field.

Instead of sending the entire **Entity**, we create a DTO to define exactly what will be sent:

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

Here, the DTO serves as an intermediary model to ensure that only necessary data is transmitted. This improves communication performance and prevents leakage of unnecessary information.

### Summary of the Opera

**Entity** Represents pure internal domain data ALWAYS, to ensure the code is decoupled from the API or database.

**Adapter** Converts data between API and Entity when the API structure is different from the app's internal structure.

**DTO** defines a specific model for transporting data between system layers when there's a need to transmit only part of the data or format it specifically.

Well, we're almost concluding our article, but I know you, reader, mentally asked me:

And the answer is simple... **Yes, we can**. I'll explain this in the next topic.

### When to use Adapter and DTO together?

In some cases, we can combine both. See a common flow:

1. The API returns data → The **Adapter** transforms the API response into an **Entity**.
2. The app needs to send data to the API → We create a **DTO** to represent exactly what will be sent.
3. The DTO can be passed to the Adapter, which then makes the necessary conversion before sending the data to the API.

This ensures well-structured, easy-to-test, and maintainable code.

![](https://cdn-images-1.medium.com/max/499/0*vhpb7CdMOGg_wBFx.gif)

### Conclusion

If there's one thing I've learned programming in Flutter (and struggling with different APIs), it's that separating code responsibilities well makes all the difference.

- **Entities** keep the code clean and independent from the API.
- **Adapters** protect the app from unexpected backend changes.
- **DTOs** ensure that only necessary data is transported.

In the end, all this makes your code more organized, scalable, and easy to test.

If you haven't structured your code this way, try it! I'm sure that once you start, you'll never want to go back.

And you, do you already use this approach? How do you structure your entities in Flutter? Let's exchange ideas here or on my networks below.

![](https://cdn-images-1.medium.com/max/480/0*SIS09iEdBEk4N9LF.gif)

Read more of my articles: [medium.com/@raphaelkennedy](https://medium.com/@raphaelkennedy)

[[ [Buy me a coffee](http://buymeacoffee.com/raphaelpontes) ]]

Follow me on social media

- LinkedIn: [raphaelkennedy](https://www.linkedin.com/in/raphaelkennedy)
- YouTube: [@raphaelpontes](https://youtube.com/@raphaelpontes)
