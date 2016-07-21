---
layout: post
title: "Interactive data visualizations in Reveal.js markdown"
description: "Interactive data visualizations in Reveal.js markdown"
author: Jan Aerts
date: 2016-07-21
categories: main
tags:
- revealjs
- dataviz
---
Although I normally use Keynote for my presentations and lectures, [reveal.js](http://lab.hakim.se/reveal-js/#/) has always been on my radar as well. One of its draws is that you can see what you're doing; which is not teh case with proprietary formats as keynote and powerpoint files. When using version control to keep track of changes to my lectures over the years, it also makes more sense to use a flat-text format than binary files.

Teaching data visualization, it's nice to include interactive visualizations directly into my presentations. Having seen it done by several people before (e.g. at the [biovis@ISMB symposium](www.biovis.net) in the beginning of July 2016), I also wanted to give it a go. It's really simple to do when using vanilla reveal.js. However, I insist on using a **markdown** file to contain my content, which makes things a bit more difficult. But got it working eventually after quite a bit of trial and error...

## Including interactive data visualizations in reveal.js markdown
You'll have to consider 3 different files for getting this to work (at least that's my setup now):

1. the index.html file
2. the markdown file containing the contents (e.g. `slides.md`)
3. the javascript file containing the code for the visualization (e.g. `viz2.js`)

### The javascript file
Let's say you want to have a slide with a visual where a green dot follows the mouse position. The javascript code for this (using the [p5 library](http://p5js.org)) could look like this:

```javascript
var viz_function = function(p) {
  p.setup = function() {
    var myCanvas = p.createCanvas(800,600)
    myCanvas.parent('viz2')
    p.noStroke()
    p.noLoop()
  }

  p.draw = function() {
    p.background(255,255,255)
    p.fill(0,255,0)
    p.ellipse(p.mouseX,p.mouseY,20,20)
  }

	p.mouseMoved = function() {
		p.redraw()
	}
}
var viz = new p5(viz_function)
```

### The markdown file

Save this code in a separate file, e.g. `viz2.js`. Notice the `myCanvas.parent('viz2')` in the `setup` function. That tells which `div` the visual should be loaded in. So we have to create that `div` in the markdown file with the slides (i.c. `slides.md`). As you can include regular html into reveal.js markdown files, you could have somethings like this:

```markdown
## New slide title

<div id="viz2"></div>

**A dot following the mouse***
```

Make sure to use the same `id` in this `div` as the one you used in the `myCanvas.parent()` function.

### The index.html file

The final thing is to load the actual code. You'll have to load the p5 library as well as the code snippet above. For including the **p5.js** library, download it from [http://p5js.org](http://p5js.org) in the directory with your `index.html` file and add this line at the end of the `head` section:

```html
<script type="text/javascript" src="p5.min.js"></script>
```

To include the script itself, add this to the `body` section, right after the line with `<script src="js/reveal.js"></script>`

```html
<script type="text/javascript" src="viz2.js"></script>
```

Any scripts for additional visualizations can be added here as well.

## Docker image
To make creating reveal.js presentations easier/quicker and incorporate this loading of scripts etc, I created a [docker image](https://hub.docker.com/r/jandot/docker-presentation/). See the link for instructions on how to use it.
