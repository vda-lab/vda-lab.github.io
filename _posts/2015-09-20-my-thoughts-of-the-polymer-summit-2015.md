---
layout: post
title:  "My thoughts of the Polymer Summit 2015"
date:   2015-09-20 10:42
author: Daniel Alcaide
categories: polymer
tags:
- polymer
---
Last Tuesday ended the Polymer Summit 2015 in Amsterdam. It was a two days event full of developers looking forward to meet other developers and to know the new announcements from the Polymer team.

[Polymer](https://www.polymer-project.org/1.0/) is a library developed by Google that implements web components. If you have never heard about that, basically web components allow us to extend the HTML vocabulary. This new tags or components depending on the context we talk, facilitate the development of web applications.

I do not regard myself a developer at all but I thought that attending to this event would be useful and enriching for the development of [Polimero](https://bitbucket.org/vda-lab/polimero), a library to create composable visualizations that VDA-Lab is currently working on.

The first day, I had the opportunity to follow the Code Lab tutorials (also available on [http://www.code-labs.io/polymer-summit](http://www.code-labs.io/polymer-summit)). As I am basically focused on data visualization I found the [data visualization code lab](http://www.code-labs.io/codelabs/polymer-webgl) the most interesting. All talks took place on Tuesday (the second day). The main ideas I took home from the talks were:

* Complex applications can be build by simpler components.
* Polymer wants you to be efficient.
* There is an element for everything.

## Complex applications can be build by simpler components

As I said before Web components facilitate development because components can be easily reused and composed. [Kevin Schaaf](https://youtu.be/jVn8tlnwAEs) gave some brief guidelines on how to think when building an app with Polymer. The first step is to break down the app you are creating in small pieces. These pieces will be much easier problems to solve ("Think locally"). The solution to resolve these smaller pieces could be a composition of other elements that we or the community have previously created ("Leveraging composition"). Because the elements work in isolated environments we should use a [mediator pattern](https://en.wikipedia.org/wiki/Mediator_pattern) to define how the elements interact between them.

## Polymer wants you to be efficient

Polymer may not be the easiest library to start with. It has lots of dependencies, importing components makes it difficult to begin for any developer who is not familiar with Polymer. [Rob Dodson](https://youtu.be/1f_Tj_JnStA) introduced [Polymer Starter Kit](https://developers.google.com/web/tools/polymer-starter-kit/). The idea behind this tool is that once downloaded, developers can start to create their app with a minimum number of tools. For example: a responsive layout, a set of components and a unit test to check the code.

The process of creating reusable components is not the same as creating web-apps and also the tools we need are different. [Addy Osmani](https://youtu.be/LMqM4PfrFxs) gave us an awesome overview about the toolkit that the Polymer team offers, starting by the structure of our own components like [Seed Element](https://github.com/polymerelements/seed-element). The optimization and efficiency are also important for them. Polybuild offers an easy solution to do that. Debugging and catching errors is a difficult part when your app has many elements. One of the most recent tools launched by Polymer team was polylint, that tries to help us to detect them before running the code.

The compatibility is one of the bases of Polymer in any app that involves many elements and our question would be: how do I test a component? [Chris Joel](https://youtu.be/kX2INPJY4Y4) presented an efficient tool for testing. It is called [Web Component Tester](https://github.com/Polymer/web-component-tester). This testing unit provides a report of the results and tests the elements in all the browsers it can find in your system.

## There is an element for everything

Google is using Polymer on multiple projects and with Polymer 1.0 they have implemented an extensive [catalog of elements](https://elements.polymer-project.org/) that solve multiple cases you will encounter when you are writing an application. In case you cannot find the element you are looking for, you can always create your own element to resolve your necessity as [Surma](https://youtu.be/qogKAkxrfrk) explained in his talk.

Some developers already had implemented elements in version 0.5 of the Polymer but these are not working anymore with the recent changes of Polymer 1.0 and 1.1. [Peter Burns](https://youtu.be/maygsoPKLpE) presented a couple of resources that facilitate the migration a lot. The first resource is the [Migration Guide](https://www.polymer-project.org/1.0/docs/migration.html) which describes the changes implemented in these newer versions of the library. The second resource is the tool called [*polyup*](https://github.com/PolymerLabs/polyup) that upgrades the majority of the components automatically. Polymer is still changing many of the elements they are publishing. If an element changes, our app maybe does not work anymore. [*polygit*](http://polygit.org/) provides all versions of a specific element.

## Conclusion

As a conclusion I believe this Polymer Summit 2015 helped me to understand how Polymer really works and to think how to use it for my work. Moreover the large and diverse community of developers that are already using this library is very motivating and inspirational to continue learning about the possibilities of web components in general and Polymer in particular.
