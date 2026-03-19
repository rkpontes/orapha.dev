---
title: "How to Integrate Flutter Modular with Flutter Bloc (Cubit) in a Simple Way and Using Custom States…"
date: '2024-05-03T16:43:03-03:00'
slug: how-to-integrate-flutter-modular-with-flutter-bloc-cubit-in-a-simple-way-and-using-custom-states
tags:
- state-management
- android-app-development
- flutter
- integration
- ios-app-development
draft: false
description: "How to Integrate Flutter Modular with Flutter Bloc (Cubit) in a Simple Way and Using Custom States (Classes) ARTICLE IN PORTUGUESE The world of Flutter libs..."
---

### How to Integrate Flutter Modular with Flutter Bloc (Cubit) in a Simple Way and Using Custom States (Classes)

[ARTICLE IN PORTUGUESE](https://medium.com/@lugpontes/como-integrar-flutter-modular-com-flutter-bloc-cubit-de-forma-simples-e-usando-estados-daf72985b24a?postPublishedType=repub)

The world of Flutter libs is constantly evolving. But what if we could combine the power of Flutter Modular with the simplicity of Flutter Bloc (Cubit)? In this article, we will explore exactly that and uncover the secrets of this powerful integration.

### Flutter Modular

Flutter Modular is a package that simplifies the organization and modularization of Flutter projects. It offers a module-based structure. In addition to providing dependency injection and route navigation.

### Cubit

Cubit is a community-developed implementation of the Bloc (Business Logic Component) design pattern in Flutter. It simplifies state management in Flutter apps, making it easier to understand and maintain. If you want to dive deeper into Cubit, check out my other article [here](https://medium.com/@lugpontes/unlocking-cubit-simplifying-state-management-in-flutter-6c3568104ba9).

### Installing the libs

This process is essential to ensure you have access to Cubit and Modular functionality in your application.

```text
flutter pub add flutter_modular flutter_bloc
```

### Modular + Cubit Integration

To integrate Flutter Modular with Flutter Bloc (Cubit), we will adopt Modular’s standard folder structure that promotes a clear separation of project modules.

**Our folder structure was organized as follows:**

| lib
| — main.dart
| — app/
| — — app_module.dart
| — — app_widget.dart
| — — home/
| — — — home_cubit.dart
| — — — home_module.dart
| — — — home_page.dart

Now to explain better, I will present the code snippets and explain the most important points.

```text
// main.dart
void main() {
  runApp(
    ModularApp(
      module: AppModule(),
      child: const AppWidget(),
    ),
  );
}
```

```text
// app_module.dart
class AppModule extends Module {
  @override
  List<Module> get imports => const [];

  @override
  void binds(Injector i) {}

  @override
  void exportedBinds(Injector i) {}

  @override
  void routes(RouteManager r) {
    r.module('/', module: HomeModule());
  }
}
```

> *6.3.3*

Module is a class from the flutter_modular package that helps organize and modularize Flutter projects.

imports: returns a list of modules that this module imports. In this case, there is no imported module ([]).

binds: is used to define module dependencies (bindings). Here, we are leaving it empty, which means we are not defining any dependencies on this particular module.

exportedBinds: is used to define dependencies that will be exported to other modules. Just like binds, we are leaving it empty in this example.

routes: The routes method is used to define the module’s routes. A route is a URL that points to a certain part of the application. Here we are setting the root route (/) to point to the HomeModule module.

In short, the app_modules.dartfile is defining the main application module (AppModule). It imports other modules, defines dependencies, exports dependencies, and configures application routes. These settings are important for organizing and structuring the project.

```text
// app_widget.dart
class AppWidget extends StatelessWidget {
  const AppWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      theme: ThemeData.light(),
      title: 'Modular Cubit Example',
      routeInformationParser: Modular.routeInformationParser,
      routerDelegate: Modular.routerDelegate,
    );
  }
}
```

The AppWidget configures and initializes the Flutter app, providing custom themes, titles, and routing settings using MaterialApp.router. This is essential to integrate Flutter Modular with Flutter Bloc (Cubit) and ensure a smooth and consistent user experience.

```text
// home_module.dart
class HomeModule extends Module {
  @override
  List<Module> get imports => const [];

  @override
  void binds(Injector i) {}

  @override
  void exportedBinds(Injector i) {}

  @override
  void routes(RouteManager r) {
    r.child(
      '/',
      child: (_) => BlocProvider(
        create: (_) => HomeCubit(),
        child: const HomePage(),
      ),
    );
  }
}
```

The HomeModule defines application-specific Home module settings, including defining routes and configuring the HomeCubit for the HomePage.

It is worth mentioning that inside r.child there is a BlocProvider that is providing HomeCubit()for the widget tree of this route. This is useful when you need a cubit class to be available to widgets within a certain route, but not globally throughout the application.

In the home_module.dart example, the BlocProvider is wrapping the HomePage. This means that any widget within HomePage that needs to access the HomeCubit will have access to it.

```text
// home_page.dart
class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    final HomeCubit homeCubit = BlocProvider.of<HomeCubit>(context);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Counter App'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            BlocBuilder<HomeCubit, CounterState>(
              builder: (context, state) {
                return Text('Counter: ${state.count}');
              },
            ),
            const SizedBox(height: 20),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                FloatingActionButton(
                  onPressed: () => homeCubit.increment(),
                  child: const Icon(Icons.add),
                ),
                FloatingActionButton(
                  onPressed: () => homeCubit.decrement(),
                  child: const Icon(Icons.remove),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
```

Inside the build method, we use BlocProvider.of<HomeCubit>(context) to get the HomeCubit instance provided by BlocProvider. This allows us to access cubit’s methods to interact with the state.

BlocBuilder is used to rebuild its children every time the state of the given cubit changes. Here, we are displaying the current counter value in the text.

FloatingActionButton defines two floating buttons: one to increment the counter when pressed and another to decrement the counter, both calling their respective methods implemented in cubit.

```text
// home_cubit.dart
class HomeCubit extends Cubit<CounterState> {
  HomeCubit() : super(CounterInitialState());

  void increment() {
    emit(CounterIncrementedState(state.count + 1));
  }

  void decrement() {
    emit(CounterDecrementedState(state.count - 1));
  }
}

// states

abstract class CounterState {
  final int count;

  CounterState(this.count);
}

class CounterInitialState extends CounterState {
  CounterInitialState() : super(0);
}

class CounterIncrementedState extends CounterState {
  CounterIncrementedState(int count) : super(count);
}

class CounterDecrementedState extends CounterState {
  CounterDecrementedState(int count) : super(count);
}
```

HomeCubit is a class that extends Cubit<CounterState>. Cubit is a class from the flutter_bloc package that manages state and business logic in a Flutter application. Here, HomeCubit manages the state of the counter.

The HomeCubit() constructor calls the constructor of the Cubit<CounterState> parent class and passes CounterInitialState() as the initial state of the cubit. This means that the initial state of the counter is CounterInitialState.

increment() and decrement() are methods used to increase and decrease the counter respectively. They use the emit method to emit new counter states based on the current state. For example, increment() emits a new state CounterIncrementedState with the counter incremented by 1 relative to the current state.

Counter states are represented by classes that extend CounterState, which is an abstract class. Each state class contains a count field, which represents the current value of the counter.

CounterInitialState represents the initial state of the counter, where the counter starts with the value 0 and is initialized together with the constructor as below.

> ***HomeCubit() : super(CounterInitialState());***

CounterIncrementedState represents the state of the counter after the increment operation, where the counter is increased by 1 from the previous state.

CounterDecrementedState represents the state of the counter after the decrement operation, where the counter is decreased by 1 compared to the previous state.

The home_cubit.dart file defines the HomeCubit cubit class responsible for managing the counter state and counter-related states, including the initial state, the state after incrementing, and the state after decrementing. It provides methods to change the counter state reactively and efficiently.

Using classes to represent states as done in the example provided has several advantages and is considered a best practice. Here are some reasons why it’s important to use classes as state:

1. Clarity and organization: Allows you to organize and structure the code in a clear and understandable way. Each state is represented by a separate class, which makes code easier to understand and maintain, especially in applications with complex states.
2. Data encapsulation: State classes encapsulate data related to a given state, making it easier to manage and manipulate. This promotes cohesion and reduces coupling between different application components.
3. Code reuse: You can reuse these classes in different parts of your application, facilitating consistency and code reuse. For example, if you have a counter state on multiple screens in your application, you can reuse the same state class on all of them.
4. Static typing: Using classes as state promotes static typing, which helps detect type errors at compile time. This provides more security and robustness to the code, reducing the likelihood of errors during execution.
5. Ease of testing: State classes are simple, independent objects that can be easily tested in isolation. This makes it easier to write unit tests to validate the application’s behavior in different states.
6. Extensibility: You can easily add new states and functionality to your application by simply creating new state classes and updating the logic accordingly. This makes the application more flexible and adaptable to future changes.

### Conclusion

Integrating Flutter Modular with Flutter Bloc (Cubit) may seem daunting at first glance, but with the right approach and the right tools, it is an achievable task. I hope this article has provided valuable insights into how to accomplish this integration. Keep exploring and experimenting to sharpen your Flutter development skills!

To learn more about Flutter Modular, check out the official documentation [here](https://pub.dev/packages/flutter_modular) and to find out more about Cubit read the documentation [here](https://pub.dev/packages/flutter_bloc) or my other article [here](https://medium.com/@lugpontes/unlocking-cubit-simplifying-state-management-in-flutter-6c3568104ba9).

Source code: [https://github.com/rkpontes/flutter_modular_cubit](https://github.com/rkpontes/flutter_modular_cubit)

Did I help you? [Buy me a coffee](https://buymeacoffee.com/raphaelpontes)

Follow me in

- **Linkedin**: [raphaelkennedy](https://www.linkedin.com/in/raphaelkennedy/)
- **Youtube:** [raphaelpontes](http://www.youtube.com/@raphaelpontes)

![](https://cdn-images-1.medium.com/max/1024/1*d4EcNSpiPllJiY5ItcDYww.png)
