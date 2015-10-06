---
layout: post
title:  "Proper syntax highlighting in Reveal.js using Pandoc"
date:   2014-01-21 19:43
author: Toni Verbeiren
categories: markdown revealjs howto
---
I use [Markdown](http://daringfireball.net/projects/markdown/) format for about everything that requires typing text, including presentations. This format is converted to the expected output format using [Pandoc](http://johnmacfarlane.net/pandoc). Since one of the later version of Pandoc, the [Reveal.js](http://lab.hakim.se/reveal-js/#/) is available as an output format which allows for very slick (HTML based) presentations. For more information on my writing workflow, please [take a look here](http://www.data-intuitive.com/2013/06/writing-workflow-markdown-pandoc-latex-and-the-likes/), the [result with a custom LaTeX style](http://www.data-intuitive.com/2013/10/activity-monitoring-from-smartphone-sensor-data-in-a-new-layout/) is available as well.

So in short, you write the presentation text and code in Markdown format in your favourite editor, convert to the reveal.js presentation format using Pandoc and you're ready. All sorts of things can be tuned, but I leave that to you to find out...

All seems well in Markdown land, but the devil is in the details...
![revealjs syntax highlight](/assets/revealjs_syntaxhighlight_small.png)

When converting to reveal.js, my code blocks were not highlighted, as should be the case because [highlight.js](http://highlightjs.org/) is included in the package. Fortunately, Pandoc can do syntax highlighting as well. </span>But the highlighting of Pandoc and the reveal.js stylesheets don't go together very well with unreadable code as a result. So I was stuck and could not get my head around why the reveal.js highlighting would not work.

I found out tonight! And the answer is very simple: the reveal.js template that is shipped with Pandoc has the appropriate highlight.js code removed. This happens in two parts: the plugin and the stylesheet are not loaded. This is probably because Pandoc ships its own highlighter.

[Attached](/assets/reveal-template.html), I have included my version of the template. In order to use it, two additional parameters have to be given to Pandoc:
```
--no-highlight --variable hlss=zenburn
```

The first one makes sure that Pandoc does not do the highlighting, the second one is a custom variable denoting the style to use for [highlight.js](http://highlightjs.org/). This is the template file to use: [reveal-template](/assets/reveal-template.html).
