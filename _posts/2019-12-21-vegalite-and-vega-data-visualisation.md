---
layout: post
title:  "Vega-Lite and Vega data visualisation tutorial"
date:   2019-12-21 12:50
author: Jan Aerts
categories: main
custom_css:
- with_exercises
tags:
- dataviz
- vega
- howto
---
This blog post acts as the hub for the vega-lite and vega tutorial taught at the EBI workshop [Data Visualisation for Biology: A Practical Workshop on Design, Techniques and Tools](https://www.ebi.ac.uk/training/events/2020/data-visualisation-biology-practical-workshop-design-techniques-and-tools-1) as well as the course material for the Data Visualisation for Data Science course at [UHasselt](https://www.uhasselt.be/studiegids?n=4&a=2019&i=4142) and [KU Leuven](https://onderwijsaanbod.kuleuven.be/syllabi/e/G0R72AE.htm#activetab=doelstellingen_idm480336).

In this tutorial, we will work in different phases, looking at vega-lite, vega, and observable. We'll start with vega-lite and vega itself in the [online editor](https://vega.github.io/editor/) that they provide, and move on to using [observable](http://observablehq.com/) at a later stage.

This tutorial is based on material provided on the vega-lite, vega and observablehq websites, as well as teaching material collected by Ryo Sakai.

* Do not remove this line (it will not be displayed)
{:toc}

## Preamble
### What are vega-lite and vega?
You might have heard of [D3](http://d3js.org) as a library to create interactive data visualisations. Indeed, this library is considered the standard in the field. Unfortunately, it does have quite a steep learning curve which makes it not ideal if you have to learn it in 2-3 days without a background in javascript programming. In this course, we'll use vega and vega-lite instead. Both are so-called _declarative_ languages, where you tell the computer _what_ you need, not _how_ to do it. Vega and vega-lite are expressed in _JSON_ ("javascript object notation"). To give you an idea, here's a small vega-lite script that shows a barchart.

{% highlight json %}
{
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "data": {
    "values": [
      {"a": "A", "b": 28}, {"a": "B", "b": 55}, {"a": "C", "b": 43}
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "b", "type": "quantitative"},
    "y": {"field": "a", "type": "ordinal"}
  }
}
{% endhighlight %}

The resulting barchart:

<img src="{{ site.baseurl }}/assets/vegalite-barchart.png" width="300px"/>

### JSON
Let's first have a look at the JSON format:

- strings are put between double quotes `"`
- numbers are _not_ put between quotes
- lists (aka arrays) are put between square brackets `[]`
- objects (aka hashes, aka dictionaries, aka key-value pairs) are put between curly brackets `{}`, and key and value are separated with a colon `:`

Also, these objects can be nested. In the example above, the whole thing is a single JSON object, consisting of key-value pairs (keys being `"$schema"`, `"data"`, `"mark"` and `"encoding"`). The `"data"` key itself holds an object `{ "values": [ ... ]}`. The `"values"` key in its place is an array of objects again.

Different elements in a JSON object or array have to be separated by a comma `,`.

## The actual tutorials
- Part 1: [Vega-lite]({{ site.baseurl }}/2019/12/vegalite)
- Part 2: Vega
- Part 3: Observable
