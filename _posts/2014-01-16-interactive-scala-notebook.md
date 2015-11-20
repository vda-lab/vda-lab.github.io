---
layout: post
title:  "Interactive (Scala) notebook"
date:   2014-01-16 14:34
author: Toni Verbeiren
categories: main
tags:
- scala
- notebook
---
When you are familiar with interactive languages like R, python, you know you get a REPL which allows you to interactively work with the language.

This has been possible with Scala (and later for Spark as well) from the beginning and it allows for some very quick way to experiment and dive into the API. Until recently, this was purely text-based., from a terminal window. There is a web-based notebook for Python: [iPython](http://ipython.org/notebook.html).

Enter [Scala-notebook](https://github.com/Bridgewater/scala-notebook). This lets you execute Scala code in the browser. But we want more... we want to render graphics in the browser...

For this, you can use a fork of the Scala-Notebook: [Scala Sketchbook](https://github.com/n8han/scala-notebook), which integrates SVG output and even D3.js!

Before compiling on a Mac, make sure you set the correct encoding:

```
export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF-8
```

Now, just follow the instructions [here](http://technically.us/sketchbook) to get the code from github and compile/run it.

And that's it. Follow along with the examples and play around with Scala in the browser. Integration with [D3.js](http://d3js.org/) is automatically included, although I did not get it working... yet.

You can find a presentation here: [http://2013.flatmap.no/hamblen.html](http://2013.flatmap.no/hamblen.html). The most interesting part is near the end.
