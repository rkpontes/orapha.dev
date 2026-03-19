---
title: "Code Generators in Flutter: What’s Cheap and What’s Expensive?"
date: '2024-06-15T16:50:54-03:00'
slug: code-generators-in-flutter-whats-cheap-and-what-s-expensive
tags:
- code-generator
- build-runner
- app-development
- flutter
- android
draft: false
description: "In the dynamic world of Flutter development, tools and libraries emerge every day, promising to make developers’ lives easier and speed up the process of cre..."
---

![](https://cdn-images-1.medium.com/max/1024/0*pDAKNdFlzpFh6Mkg.png)

In the dynamic world of Flutter development, tools and libraries emerge every day, promising to make developers’ lives easier and speed up the process of creating applications. Among them, code generators stand out for their ability to automate repetitive tasks and generate boilerplate code, freeing up time for what really matters: business logic and user experience.

But is this promise of productivity and efficiency really all it seems? Could it be that code generators bring with them some challenges and disadvantages that can, in the long run, compromise the quality and sustainability of your code?

In this article, we will delve into this controversy and analyze the pros and cons of code generators in Flutter, exploring tools such as MobX, Riverpod, Injectable, AutoRoute and others that rely on build_runner to generate code. We will address the points of view that defend the practicality and agility provided by these tools, but we will also give voice to the critics who warn of the dangers of “cheap that ends up being expensive”.

### 1. The “Program a Little, Generate a Lot” Dilemma

![](https://cdn-images-1.medium.com/max/599/0*u-5VlRe5Mn4OedZi.jpg)

In the fast-paced world of Flutter development, code generators are a powerful ally in the battle against repetitive and tedious tasks. By automating the creation of getters, setters, constructors, and other boilerplate elements, these tools free up valuable time for developers to focus on the most crucial aspects of code: business logic and user experience.

However, this rampant automation can bring with it an undesirable side effect: code disconnection. When developers move away from writing each line of code by hand, they can move away from deeply understanding how the internals work. This lack of familiarity can create a number of challenges down the road, including:

- **Difficulty debugging:** Imagine a mysterious bug in your code. Without a complete understanding of how the generated code works, the investigation becomes a maze with no exit, delaying the resolution process and frustrating developers.
- **Long-term maintenance:** a guaranteed nightmare: Time passes, features evolve, and the need to modify the code arises. But how can you do this if you don’t remember the details of the original implementation? Over-reliance on code generators can turn maintenance into a nightmare, consuming valuable time and resources.
- **Loss of autonomy and creativity:** Excessive automation can stifle developers’ creativity and autonomy. By sticking to rigid, predefined patterns, they lose the flexibility to explore innovative and customized solutions, limiting the project’s potential.

It is important to remember that code is the lifeblood of your application. Understanding it thoroughly is crucial to ensuring its evolution, stability and security. Automation, when used consciously and in a balanced way, can be a valuable tool. But never let it take the place of your developers’ expertise and knowledge.

To avoid the dangers of excessive automation, it is essential to adopt a conscious and balanced approach:

- **Use code generators sparingly:** Use them to automate only tedious and repetitive tasks, preserving the opportunity to write and understand critical code manually.
- **Prioritize comprehension:** Don’t just “paste” the generated code into your project. Take the time to understand how it works and how it integrates with the rest of the code.
- **Encourage collaboration:** Promote discussion and knowledge sharing among team members, ensuring that everyone is familiar with the code and the tools used.

### 2. Coupling: A Hidden Trap

![](https://cdn-images-1.medium.com/max/800/0*lql9ReLLSSnTwFu-.jpg)

In the world of software development, coupling is like an invisible web that connects different parts of the code. When used well, it can bring organization and modularity to a project. However, excessive coupling can turn into a treacherous trap, especially when it comes to code generators.

By delegating the generation of essential parts of your code to external tools, you create a strong dependency on them. This means that, for any modification or customization in the future, you will be intrinsically tied to the rigid rules and standards of these generators.

Suppose you decide to change the structure of your project or implement an innovative feature that does not fit into the pre-packaged boxes of code generators. In this scenario, you will be faced with two options:

- **Submit to Rigid Rules:** Adapt your new idea to the inflexible standards of code generators, sacrificing the flexibility and customization you craved. This option can be frustrating and lead to suboptimal solutions, limiting the potential of your project.
- **Break the Chains:** Face the arduous challenge of modifying the generated code manually, navigating a maze of abstractions and unknown dependencies. This journey can be time-consuming, complex, and error-prone, consuming precious time and resources.

In both cases, excessive coupling can be an obstacle to the evolution of your project. It limits your creative freedom, makes maintenance difficult, and prevents you from responding to changes with agility and flexibility.

To escape the coupling trap and ensure the freedom and sustainability of your code, there are a few steps you can take:

- **Prioritize Modularity:** Organize your code into well-defined, independent modules, minimizing interdependencies between them. This makes it easier to modify a module without affecting the rest of the project.
- **Use Interfaces and Abstractions:** Create interfaces that define contracts between modules, allowing you to replace concrete implementations without compromising the overall structure of the code.
- **Avoid Direct Dependencies:** Avoid having modules directly depend on other modules. Use mechanisms such as dependency injection to decouple classes and facilitate testing and code reuse.
- **Evaluate Tools Carefully:** If you have no other options, choose code generators that offer flexibility and customization options, allowing you to adapt the generated code to your specific needs.

### 3. Limited Customization: A World of Restrictions

![](https://cdn-images-1.medium.com/max/800/0*gsQHtKHubwIgcDp0.jpg)

In the world of software development, customization is like the soul of code: it allows you to bring your ideas to life, tailor solutions to your specific needs, and create something unique and distinctive. But when it comes to code generators, this creative freedom can turn into a prison of restrictions.

While code generators offer some configuration options, this flexibility is often limited to rigid, predefined standards. This means that you may find yourself forced to follow a predetermined path, even if it doesn’t perfectly align with your vision and the needs of your project.

Imagine that you have an innovative idea for a feature, but the code generator doesn’t support its implementation. Or that you want to customize the style of your code to reflect your brand identity, but the generator’s rigid standards prevent you from doing so.

In these cases, frustration sets in. You feel trapped in a golden cage, unable to explore the full potential of your code and bring your ideas to life the way you truly want.

The lack of customization of code generators can have several negative consequences for your project:

- **Difficulties in Implementing Specific Functionalities:** Implementing complex or customized functionalities can become a difficult challenge, requiring complex adaptations and workarounds to get around the generator’s limitations.
- **Difficulties in Code Maintenance and Evolution:** In the long term, the lack of customization can make it difficult to maintain and evolve the code, making it inflexible and difficult to adapt to the project’s new needs.

Customization is key to creating unique, differentiated solutions that truly meet your needs. Don’t settle for the limitations of code generators.

Explore alternatives, seek creative solutions, and fight for the freedom to bring your ideas to life the way you’ve always dreamed.

### 4. The Promises of Macros in Flutter: An Alternative Solution?

![](https://cdn-images-1.medium.com/max/1024/0*Wm7rZs1MoOa6kOLG.jpg)

Flutter is constantly evolving, and with it comes new tools and technologies that promise to offer more flexible and customizable solutions for code generation. Macros, for example, are a promising technology that can bring new horizons to this area.

Macros stand as a beacon of innovation, opening up a new world of possibilities for creating unique solutions tailored to your needs.

Unlike traditional code generation tools, macros give developers the power to define their own patterns and rules for code creation, even before compilation. This means that you, as a developer, take full control over the customization of the generated code, freeing yourself from the rigid and predefined constraints that so limit creativity and innovation.

#### Unlocking the Power of Macros: Practical Examples

To illustrate the power of macros, let’s explore some practical examples of how they can be used in your day-to-day life:

- **Custom Widget Creation:** Create reusable widgets with specific styles and behaviors, standardizing your application’s interface and saving time in development.
- **Custom Boilerplate Code Generation:** Say goodbye to repetitive and boring code. Generate custom boilerplate code that perfectly fits your needs, optimizing your workflow.
- **Implementation of Complex Business Rules:** Transform your project’s business rules into macros, making the code easier to read, maintain and reuse.
- **Automation of Repetitive Tasks:** Automate tedious and repetitive tasks, freeing up time for you to focus on more strategic and creative activities.

#### But how do macros work in practice?

Macros in Flutter are implemented as special classes that can intercept and modify source code before compilation. This means that you can define your own rules and patterns for code generation, using the Dart language to write macros.

To use macros in Flutter, you need to enable experimental mode in your project configuration. In addition, it is important to have a good knowledge of the Dart language to be able to write macros efficiently and safely.

**Remember:** macros are powerful tools that, when used wisely, can transform your software development process, taking it to a new level of efficiency, quality, and creative freedom. Explore this innovative technology and embrace the power of unlimited customization!

To deepen your knowledge about macros in Flutter, check out the official documentation: [https://dart.dev/language/macros](https://dart.dev/language/macros)

#### Extra Tips:

- Use macros sparingly and avoid creating complex, hard-to-understand code.
- Test your macros carefully to ensure they work properly and don’t cause problems in your code.
- Share your macros with the community so other developers can benefit from them.

### Conclusion

Flutter code generators can be valuable tools that can increase productivity and speed up the development process. However, it is important to use them with caution and be aware of their limitations and drawbacks.

Before adopting any code generation tool, carefully evaluate your specific needs and the challenges it may bring. Look for solutions that offer flexibility and customization, and be prepared to deal with increased coupling and potential unfamiliarity with the generated code.

After all, “you get what you pay for” can be a reality in the world of software development. Evaluate all options carefully and make conscious and informed choices that ensure the quality, sustainability, and flexibility of your code in the long run.

**Did I help you?** [Buy me a coffee](https://buymeacoffee.com/raphaelpontes)

**Follow me in**

- **Linkedin**: [raphaelkennedy](https://www.linkedin.com/in/raphaelkennedy/)
- **Youtube:** [raphaelpontes](http://www.youtube.com/@raphaelpontes)
