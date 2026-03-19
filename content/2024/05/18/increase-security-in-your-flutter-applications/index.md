---
title: "Increase security in your Flutter applications"
date: '2024-05-18T00:01:19-03:00'
slug: increase-security-in-your-flutter-applications
tags:
- security
- android
- ios
- development
- flutter
draft: false
description: "In today’s digital world, application security is an absolute priority. Developing a robust and secure Flutter app is crucial to protecting user data and mai..."
---

![](https://cdn-images-1.medium.com/max/696/0*TRlO7z09Bs7U1b8I.jpg)

In today’s digital world, application security is an absolute priority. Developing a robust and secure Flutter app is crucial to protecting user data and maintaining trust in your product. If you are starting your Flutter application security journey, I recommend starting by reading my previous article, where I explore essential practices in Gray Box mode to ensure the security of your application ([link to article](https://raphaelkennedy.medium.com/ensuring-the-security-of-your-flutter-application-essential-practices-in-gray-box-mode-09dd58651727)).

### Security Analysis: Key Findings

During the security assessment of Flutter applications, together with my experience in the market, I identified several steps that allow locating possible vulnerabilities, which I will talk more about below.

#### Authentication Review

We examine the authentication mechanisms used in applications. We identified that the absence of a robust security mechanism during authentication resulted in the generation of user tokens containing sensitive data in clear text. To be clear, JWT tokens can be decrypted if they are not issued in the right way. On the jwt.io website, it allows you to paste your token and they will present all the internal data.

![](https://cdn-images-1.medium.com/max/1024/1*w_RtZeqJkH-TNuDZ0BX5dg.png)

_Figure 1 — capture from JWT.io website_

![](https://cdn-images-1.medium.com/max/1024/1*UZIfY-Hssq4hDfx_7OqgcA.png)

_Figure 2 — Data obtained with token decoding_

In Figure 1, you can see a JWT token added to the website and Figure 2 presents the decompiled data. It is worth highlighting the practice of using security keys that help decode this token where only the server uses it to compile and the app-client to decompile, as shown in Figure 3 below.

![](https://cdn-images-1.medium.com/max/1024/1*mktuzuWKv69Cj1N3E_zllQ.png)

_Figure 3 — Secret key location 256 bits_

#### Assessment and Mitigation of Failures in Access Controls

Another important point to note is the access controls on the front-end, where we can discover several significant flaws. These flaws allow the application to be accessed on devices considered insecure, that is, specifically those that have been jailbroken or rooted.
These devices pose a greater risk because they are overly permissive, meaning they allow you to perform actions and install applications without the security restrictions imposed by standard operating systems. In such environments, application security mechanisms can be easily bypassed, exposing sensitive data and critical functionality to potential attackers. This highlights the need to implement more stringent security controls on the front end to detect and block access from compromised devices.
To overcome access control flaws in Flutter and protect your application on insecure devices, you can adopt several strategies. It is important to implement detection of these devices. In Flutter, there are specific libraries that help identify whether the device is compromised. When detecting a jailbroken or rooted device, you can choose to display a warning message to the user and block access to the app, ensuring it cannot function.
Another crucial measure is to check the integrity of the environment in which the application is running. This may include detecting emulators and verifying that the application binary has not been tampered with. To do this, it is possible to use digital signature and checksum verification techniques, ensuring that the application code remains unchanged.

Additionally, it is essential to encrypt all sensitive data that is stored locally. Using secure encryption libraries prevents data from being stored in clear text, protecting sensitive information even if the device is compromised. The flutter_secure_storage package, for example, offers a secure way to store encrypted data in Flutter.

Finally, it is important to implement strict server-side security policies. Ensuring that the server validates all requests independently of any checks made on the client is essential. The server must reject requests that do not meet established security criteria, adding an extra layer of protection against possible attacks.

#### Failure of the Anti-Tampering Mechanism

Another important point is to check that when decompiling the application for Android, it is possible to change the source code and recompile the application. To do this, we can use tools such as APKTOOL to decompile the APK and modify the Java code obtained. After this process, we were able to change the variables using a text editor such as Sublime Text. After changing the code, we were able to recompile and sign the application with the same APKTOOL. Once these processes are complete, we can verify that the changes made to the source code were present in the recompiled application.
This vulnerability allows an attacker to understand the internal workings of the application through reverse engineering, enabling the development of attacks on security mechanisms. The attacker can add new unauthorized features, which is very common nowadays in apps such as Whatsapp or Youtube, in order to prevent messages from being deleted by the user who sent them and even displaying advertisements, in addition, it can lead to data theft, damage to the company’s reputation and image, as well as fraud.
To mitigate this risk, it is recommended that the application is capable of detecting, at runtime, any modifications to the code made during compilation. The application must identify compromised environments and react accordingly, either by reporting the breach to the server or shutting down the application. Implementing these measures is crucial to protect the application against tampering attempts and ensure the integrity and security of user data.

Well, these were some points that I identified along my journey, I invite you to study more about security in Flutter applications. Explore available resources, participate in cybersecurity workshops, courses and forums. Security is a shared responsibility and it is essential that we all educate ourselves and be prepared to face the ever-changing challenges of the digital world.
Remember, security is not a destination, but rather an ongoing journey. Together, we can make our Flutter apps safer and more secure for all users.
Study, learn and let’s build a safer digital future, application by application.

Did I help you? [Buy me a coffee](https://buymeacoffee.com/raphaelpontes)

Follow me in

- **Linkedin**: [raphaelkennedy](https://www.linkedin.com/in/raphaelkennedy/)
- **Youtube:** [raphaelpontes](http://www.youtube.com/@raphaelpontes)
