---
layout: post
title:  "From interactive to interactivated visualizations"
date:   2014-10-17 08:10
author: Toni Verbeiren
categories: d3
tags:
- d3
---
I've been into generating documents and graphs from data (and source) since I started working on [my PhD](http://itf.fys.kuleuven.be/_binary/publications/phd_stat/2003_toni_verbeiren.pdf), which is like 15 years ago by now. Back then, I used [MetaPost](http://en.wikipedia.org/wiki/MetaPost) for generating PostScript figures to include in the thesis. The benefits of not using any of the available interactive tools ([xmgr](http://en.wikipedia.org/wiki/Grace_(plotting_tool)) comes to mind) were and still are plentiful. Besides being able to create figures that exactly match the font and style of the document for which they're created, I could easily make style changes on all the graphs simultaneously using a few key strokes. Obviously (at that time) the document itself was generated using LaTeX.

## Static Visualizations
The last couple of years a lot has happened concerning both marking up documents, but also rendering graphs and visualizations. I have been using [Markdown](http://daringfireball.net/projects/markdown/) and [RMarkdown](http://rmarkdown.rstudio.com/) [extensively](http://www.data-intuitive.com/2014/09/writing-workflow-and-reproducible-data-analysis/) in the past, both for rendering (publication ready) [PDF documents](http://www.data-intuitive.com/2013/10/activity-monitoring-from-smartphone-sensor-data-in-a-new-layout/) as for [a quick export to html](http://tverbeiren.github.io/ReproducibleDataAnalysis/RR.html) and even for [creating presentations](http://tverbeiren.github.io/BigDataBe-Spark/#/).

RMarkdown in combination with [knitr](http://yihui.name/knitr/) lets you include programming code to be executed in-place in a document. The output of the code (text, table, graph, ...) is included in the document. This is very much like how I created the MetaPost figures for my PhD thesis, with the exception that the code still lived outside of the source document.

Most of what I have been doing with these tools is static, but more and more, interactivity becomes important. Especially if you think in the context of Visual Analytics, user interaction may be the differentiating factor. Obviously, a PDF document is too static. Let us turn then to the web...

## Dynamic Visualizations
The web is made for interactivity. Either via middleware that runs in the browser (Java, Flash, ...) or by means of Javascript that runs natively. My impression is that [D3.js](http://d3js.org/) is becoming the standard in Javascript frameworks for interactive visualizations. Many Javascript visualization libraries are built on top of D3:  [RickShaw](http://code.shutterstock.com/rickshaw/), [Epoch](http://fastly.github.io/epoch/), [Dimple](http://dimplejs.org/), [ParCoords.js](http://syntagmatic.github.io/parallel-coordinates/), etc. There are others libraries besides D3, but they do not yet have the same community around them: [P5.js](http://p5js.org/), [Bokeh.js](https://github.com/ContinuumIO/bokehjs), [Tableau](http://www.tableausoftware.com/new-features/javascript-api), ...

With all these nice tools and frameworks for (interactive) visualization, why would you still write the code for those things in a text editor? Why not move the development environment to the browser as well? But still keeping text and code (and the result of the code) together.

This can be done using so-called notebooks. Examples are [IPython](http://ipython.org/notebook.html), [IJulia](https://github.com/JuliaLang/IJulia.jl), [Scala-notebook](https://github.com/Bridgewater/scala-notebook), [Spark-notebook](https://github.com/andypetrella/spark-notebook), [RNotebook](https://github.com/ramnathv/rNotebook), etc. Those are fun things to work with. You can combine text, code, figures, etc. and run the code interactively. This way, using the proper visualization library, it is possible to create visualizations immediately in D3 for use in the browser.

## Interactivated Visualizations
All the above is nice, but when a graph is created all (at least as far as I know) visualization libraries that work in a notebook ([matplotlib](http://matplotlib.org/) for Python to name one) render static images that are shown in the notebook window. In other words, there is no interactivity. Even no simple zooming or panning! The conclusion is that *all* interactivity should be explicitly coded in the appropriate D3 way. Why then use a notebook?

Now, take a look at what [mpld3.js](http://mpld3.github.io/) does: it converts a matplotlib-rendered vizualization into a D3 visualization. *Boom!* It's as simple as that. By translating the functions into D3 code and rendering the resulting visualization in the notebook, we immediately get an interactive graph instead of a static image. The only thing to be changed to the code for the visualization is adding one line in the beginning.

Granted, zooming and panning are not terribly useful in all situations. But other modes of interactivity are possible as well by means of plugins that code for specific interactions.

To me, this is a huge step forewards: no need to learn D3 for creating basic interactive visualizations for the browser, just translate what you have and know to D3.

Are you familiar with similar libraries, please do not hesitate to tell us!

*For completeness*: It is possible to turn RMarkdown documents into interactive visualizations as well, using R and Shiny, for instance.  
