---
layout: post
title:  "Hands-on data visualization using svelte"
date:   2021-03-03 19:52
author: Jan Aerts
categories: main
use_math: true
tags:
- dataviz
- svelte
- howto
---
This is a svelte ([http://svelte.dev](http://svelte.dev)) version of the Processing/p5/vega tutorials that we published earlier. Svelte is a framework for creating web content, and very accessible for creating data visualisations. This tutorial holds numerous code snippets that can by copy/pasted and modified for your own purpose. The contents of this tutorial is available under the CC-BY license.

![cc-by]({{ site.baseurl }}/assets/ccby.png)

## Table of contents                                                            

* Do not remove this line (it will not be displayed)                            
{:toc}

## What is Svelte?
Svelte is a framework for building webpages. It makes it easier to build complexer websites, but is also a very good fit for data visualisation using SVG.

<img src="{{ site.baseurl }}/assets/svelte_logo.png" />

One of the strong points of Svelte is that it makes creating different components very simple, although we will not use these initially. Nevertheless, just to give you an idea, below is a simple example. The `#each` and curly brackets will be new to you, but you should get the idea. In the top version of this code we create 2 different scatterplots where we create an `svg` and write the code to loop over the datapoints two times (once for each dataset). Using Svelte, we can however easily create a `Scatterplot` HTML element which simplifies the main code a lot.

{% highlight html %}
<h1>My plot</h1>
<svg width=400 height=400 data={dataset1}>
  {#each data as datapoint}
    <circle cx={datapoint.x} cy={datapoint.y} r=20 />
  {/each}
</svg>

<svg width=400 height=400 data={dataset2}>
  {#each data as datapoint}
    <circle cx={datapoint.x} cy={datapoint.y} r=20 />
  {/each}
</svg>
{% endhighlight %}

{% highlight html %}
<h1>My plot</h1>
<Scatterplot data={dataset1} />
<Scatterplot data={dataset2} />
{% endhighlight %}

The svelte website has a _very_ good tutorial, available at [https://svelte.dev/tutorial](https://svelte.dev/tutorial). We really recommend going through at least sections 1 through 7 (Introduction, Reactivity, Props, Logic, Events, Bindings, and Lifecycle). A lot of what follows below is based on that material, but with an emphasis on data visualisation.

### HTML, CSS and javascript
In order to follow this tutorial, you have to understand that:

- HTML: provides the basic structure of the page, which can be enhanced using CSS and javascript. All HTML elements on a webpage together are called the Document Object Model or DOM.
- CSS: is used to control presentation, formatting and layout: what it _looks_ like. The CSS is denoted by the `<style></style>` tags.
- javascript: is used to control the _behaviour_ of different elements and the page as a whole. The javascript section in a svelte file is surrounded by `<script></script>` tags.

You should have at least a little knowledge of what HTML is and how it works for the rest of this tutorial.

A Svelte file can contain the HTML, CSS and javascript together. Here is a very simple `App.svelte` that includes all three of them:

{% highlight html %}
<script>
  let name = 'World'
</script>

<style>
  h1 {
    color: green;
  }
</style>

<h1>Hello {name}!</h1>
{% endhighlight %}

In this example, we get a heading of level 1 (`h1`) that is green (as defined in the `<style>` element), and says "Hello World!" where the "World" is defined in the javascript section.

### Using the Svelte REPL
Before we start creating files on our own machine and run a local server, we will look at the online svelte REPL (Read-Eval-Print-Loop), available at [http://svelte.dev/repl](http://svelte.dev/repl).

<img src="{{ site.baseurl }}/assets/svelte-repl.png" width=800 />

On the REPL, you have the code at the left and the result at the right. At the image above there is only one file that you have to change at the moment, called `App.svelte`.

The first time you open the REPL you will get the following code:
{% highlight html %}
<script>
	let name = 'world';
</script>

<h1>Hello {name}!</h1>
{% endhighlight %}

When you open that REPL link for the first time, you'll be greeted with the following code:

You can clearly see the 3 different sections that can make up a svelte file:
- script: denoted by `<script></script>` tags
- CSS: denoted by `<style></style>` tags
- html: the rest (in this case consisting of an `h1` and an `svg` element)

The image above shows how these 3 parts work together. Let's start with the HTML and see where the `script` and `style` parts come into play.

So let's start creating data visualisations.

## Scalable Vector Graphics
Scalable Vector Graphics (or SVG for short) are a way to create data visualisation in HTML pages. HTML has default elements such as `h1` (header of level 1), `ul` (unordered list), `p` (paragraph), etc. Within an `svg` element you can use elements such as `circle`, `rect` (rectangle) and so on. For a full list of elements you can use within `svg`, see [here](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg).

Remove all code in the `App.svelte` on the REPL, and replace it with the following:

{% highlight html %}
<svg width=400 height=400>
  <circle cx=100 cy=100 r=15 />
  <circle cx=150 cy=75 r=20 />
  <rect x=250 y=300 width=30 height=20 />
</svg>
{% endhighlight %}

You should now see a picture with 2 black circles and a rectangle.

## Styling
Just black circles and rectangles aren't that nice. Let's give them some colour. We can do that using CSS. There are different places where you can define the CSS (inline, in the header, in a separate file), but in svelte this is normally done in a separate `<style></style>` section. Let's add this `style` section to the script that you already have:

{% highlight html %}
<style>
  circle {
    fill: steelblue;
  }
  rect {
    fill: green;
    stroke: red;
    stroke-width: 3;
  }
  svg {
    background-color: whitesmoke;
  }
</style>

<svg width=400 height=400>
  <circle cx=100 cy=100 r=15 />
  <circle cx=150 cy=75 r=20 />
  <rect x=250 y=300 width=30 height=20 />
</svg>
{% endhighlight %}

We now have a slightly nicer picture with blue circles and a green rectangle (with a red border). We've also given the SVG element itself a very light background so that we can see how big it is.

This is the image we now have:

<img src="{{ site.baseurl }}/assets/svelte-2circles1rect.png" width=400 />

### CSS Selectors
All the HTML elements we've used can have _attributes_, such as `cx` and `cy` for `circle` elements, and `width` for `svg` elements. Each element has a specific list of possible attributes (check their documentation), but you can also add your custom attributes if you want. There are however two special ones: `id` and `class`.

- `id`: The `id` attributes gives the element a specific - you guessed it - ID. That can be used in your `script` and `style` sections to identify a specific element.
- `class`: The `class` attribute assigns that element to a certain class (or group). We can use this to easily select different elements together. We can for example have a todo list where some of the tasks have been completed.

{% highlight html %}
<ul>
  <li id="todo1" class="completed">Go shopping</li>
  <li id="todo2" class="completed">Work out</li>
  <li id="todo3">Read in my book</li>
  <li id="todo4" class="completed">Pay taxes</li>
</ul>
{% endhighlight %}

In the `style` sections that we showed above, we used the element type (i.e. `circle`, `rect` and `svg`) to identify which elements a certain style should be applied to. We can also use the id and class, though.

- To refer to an element with a specific ID, prepend that ID with a hash tag in the CSS.
- To refer to all elements of a certain class, prepend that class with a period in the CSS.

For example:

{% highlight html %}
<style>
  #todo2 {
    color: red;
  }
  .completed {
    opacity: 0.2
  }
</style>

My todo list:
<ul>
  <li id="todo1" class="completed">Go shopping</li>
  <li id="todo2" class="completed">Work out</li>
  <li id="todo3">Read in my book</li>
  <li id="todo4" class="completed">Pay taxes</li>
</ul>
{% endhighlight %}

will result in:

<img src="{{ site.baseurl }}/assets/svelte-css-selectors.png" width=200 />

As you can see, all items that are completed are greyed out.

You can also combine CSS selectors. For example, to target `li` elements that have the class `completed`, but not any other element with that same class, we can use the selector `li.completed`.

CSS selectors are a very powerful way to select elements in an HTML page. They for example also one of the cornerstones when you want to create data visualisations in [D3](http://d3js.org). For a full list, see [here](https://www.w3schools.com/cssref/css_selectors.asp).

## Looping over datapoints
Say we have a dataset of 10 datapoints, and we want to plot them all (like a scatterplot). One way of doing this would be:

{% highlight html %}
<svg width=400 height=400>
  <circle cx=100 cy=100 r=5 />
  <circle cx=150 cy=275 r=5 />
  <circle cx=10 cy=101 r=5 />
  <circle cx=80 cy=183 r=5 />
  <circle cx=350 cy=45 r=5 />
  <circle cx=201 cy=285 r=5 />
  <circle cx=150 cy=306 r=5 />
  <circle cx=90 cy=102 r=5 />
  <circle cx=73 cy=39 r=5 />
  <circle cx=332 cy=269 r=5 />
</svg>
{% endhighlight %}

<img src="{{ site.baseurl }}/assets/svelte-svg-hardcoded.png" width=400 />

It doesn't make sense to hard-code the different circles in the HTML itself. It'd be better to define them as an array of data and loop over them.

In the `script` section, let's define a variable `data`:

{% highlight html %}
<script>
  let datapoints = [{x: 100, y: 100},
                    {x: 150, y: 275},
                    {x: 10, y: 101},
                    {x: 80, y: 183},
                    {x: 350, y: 45},
                    {x: 201, y: 285},
                    {x: 150, y: 306},
                    {x: 90, y: 102},
                    {x: 73, y: 39},
                    {x: 332, y: 269}]
</script>
{% endhighlight %}

The `svg` part can now be populated programmatically like this:

{% highlight html %}
<svg width=400 height=400>
  {#each datapoints as datapoint}
    <circle cx={datapoint.x} cy={datapoint.y} r=10 />
  {/each}
</svg>
{% endhighlight %}

### Conditional logic
Here we see for the first time how we can add _logic_ (like conditionals and loops) in HTML in svelte. Normally, HTML does not allow this but svelte does provide that functionality. To add this logic in the HTML part of a svelte file, we put these commands between curly brackets `{` and `}`. Whereas in regular javascript an `if` conditional looks like this:

{% highlight javascript %}
if ( value > 10 ) {
	# do something
} else {
	# do something else
}
{% endhighlight %}

In svelte this looks like:

{% highlight html %}
{#if value > 10 }
  # show a certain HTML element
{:else}
  # show another HTML element
{/if}
{% endhighlight %}

### Loop logic
Loops are similar, using the `each` command. In regular javascript:

{% highlight javascript %}
datapoints.forEach(function(datapoint) {
  # do something with datapoint
})
{% endhighlight %}

In svelte this looks like:

{% highlight html %}
{#each datapoints as datapoint}
  # create HTML element for this datapoint
{/each}
{% endhighlight %}

Again: see the [svelte tutorial](https://svelte.dev/tutorial) for another explanation of this, including `else if`, etc.

IMPORTANT: Note that this syntax is for the HTML part of a svelte file, _not_ for the script part which is regular javascript.

Back to the data visualisation we are building. We now get the same picture again, but didn't have to specify the separate datapoints within the HTML anymore.

Our full script now looks like this:

{% highlight html %}
<script>
  let datapoints = [{x: 100, y: 100},
                    {x: 150, y: 275},
                    {x: 10, y: 101},
                    {x: 80, y: 183},
                    {x: 350, y: 45},
                    {x: 201, y: 285},
                    {x: 150, y: 306},
                    {x: 90, y: 102},
                    {x: 73, y: 39},
                    {x: 332, y: 269}]
</script>

<style>
	svg {
		background-color: whitesmoke;
	}
	circle {
    fill: steelblue;
  }
</style>

<svg width=400 height=400>
  {#each datapoints as datapoint}
    <circle cx={datapoint.x} cy={datapoint.y} r=10 />
  {/each}
</svg>
{% endhighlight %}


For argument's sake, let's add an `if` statement as well: we'll add a value to all these points, and let the visual encoding (circle or rectangle) be dependent on that value.

{% highlight html %}
<script>
  let datapoints = [{x: 100, y: 100, value: 9},
                    {x: 150, y: 275, value: 11},
                    {x: 10, y: 101, value: 72},
                    {x: 80, y: 183, value: 2},
                    {x: 350, y: 45, value: 10},
                    {x: 201, y: 285, value: 109},
                    {x: 150, y: 306, value: 24},
                    {x: 90, y: 102, value: -4},
                    {x: 73, y: 39, value: 88},
                    {x: 332, y: 269, value: 8}]
</script>

<style>
  svg {
    background-color: whitesmoke;
  }
  circle {
    fill: steelblue;
  }
  rect {
    fill: red;
  }
</style>

<svg width=400 height=400>
  {#each datapoints as datapoint}
    {#if datapoint.value > 10}
      <circle cx={datapoint.x} cy={datapoint.y} r=10 />
    {:else}
      <rect x={datapoint.x} y={datapoint.y} width=10 height=10 />
    {/if}
  {/each}
</svg>
{% endhighlight %}

In this example, we embedded an `if` statement within the `each` loop. This is the picture that we get:

<img src="{{ site.baseurl }}/assets/svelte-ifelse.png" width=400 />

## Running svelte locally
Although extremely useful, you will at some point outgrow the REPL that we've used up to now. Still, you might go back to it regularly to quickly test something out.

We can also develop svelte applications (i.c. visualisations) locally, on our own machine. See the [Getting Started for new developers](https://svelte.dev/blog/svelte-for-new-developers) page on how to get set up.

Although it is out of scope for this tutorial, it comes down to running `npx degit sveltejs/template my-new-project`, and running `npm install` in the new `my-new-project` folder. When that's finished you can run `npm run dev` which will make the application available on http://localhost:5000 and automatically reload that page when you make changes to any of the files.

## Loading data
Data visualisation relies on data. We can load data in several ways in javascript.

### In the `script` section
We've already seen above how to define datapoints within the `script` section of a svelte file, so we'll skip that here.

### In a separate `.js` file
You can also create a new file, e.g. called `data.js` which has the following form:

{% highlight javascript %}
export default [
  {"name": "Thigpen", "city": "Bay Springs", "state": "MS", "country": "USA", "lat": 31.95376472, "long": -89.23450472, "vip": false},
  {"name": "Livingston Municipal", "city": "Livingston", "state": "TX", "country": "USA", "lat": 30.68586111, "long": -95.01792778, "vip": false},
  {"name": "Meadow Lake", "city": "Colorado Springs", "state": "CO", "country": "USA", "lat": 38.94574889, "long": -104.5698933, "vip": false},
  ...
]
{% endhighlight %}

See this screenshot of the REPL where there is both an `App.svelte` and the newly-created `data.js`. To access that data from the svelte file, use

{% highlight javascript %}
  import datapoints from 'data';
{% endhighlight %}

A full example would be:
{% highlight html %}
<script>
  import datapoints from 'data'
</script>

<h1>Airports in the US</h1>
<ul>
  {#each datapoints as datapoint}
    <li>{datapoint.name} - {datapoint.state}</li>
  {/each}
</ul>
{% endhighlight %}

You can also give the data a name in the `data.js` file. Either:
- use `import datapoints from './data'` in `App.svelte` and `export default [...]` in `data.js`, or
- use `import { flights } from './data'` in `App.svelte` and `export const flights = [...]` in `data.js`

Notice that in the former case we make the data available through the variable `datapoints` (defined in `App.svelte`), versus the variable `flights` (defined in `data.js`).

### From an online CSV file
To be able to load external data in CSV format, we have to install the [PapaParse](http://www.papaparse.com) npm package. To do so:
- Stop the `npm run dev` server.
- Run `npm install papaparse` in the root folder of your svelte application.
- Restart `npm run dev`.

Here's a working example using data about Belgian beers.

{% highlight html linenos %}
<script>
  import Papa from 'papaparse';

  let datapoints = [];
  Papa.parse("http://vda-lab.github.io/assets/beers.csv", {
    header: true,
    download: true,
    complete: function(results) {
      datapoints = results.data
    }
  })
</script>

<ul>
  {#each datapoints.slice(1,20) as datapoint}
    <li>{datapoint.Merk} ({datapoint.Soort})</li>
  {/each}
</ul>
{% endhighlight %}

Let's walk over this code:
- line 2: import the `PapaParse` package
- line 4: define a default value (i.e. empty array) for the `datapoints` variable
- lines 5-11: this is where we load data into that variable. See the [PapaParse documentation](http://www.papaparse.com) documentation about the configuration options you can use. In this case, we take the `results` when parsing is `complete` and copy it into the `datapoints` variable in line 9. Try adding a `console.log(results)` just before line 9 to see what the `results` object looks like in the console.

### From an online JSON file
If the remote file you're trying to read is in JSON format, we don't need the PapaParse package but can use the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) instead. Here's the code to load a remote JSON file:

{% highlight html %}
<script>
  let datapoints = [];
  fetch("http://vda-lab.github.io/assets/beers.json")
    .then(res => res.json())
    .then(data => datapoints = data)
</script>

<ul>
  {#each datapoints as datapoint}
    <li>{datapoint.beer}</li>
  {/each}
</ul>
{% endhighlight %}

### In a local csv or json file
The above CSV and JSON files are on a remote server. But what if we have the data on our own machine? Actually, this is very simple as we are running our own server. If you put the data file in the `public` directory of your svelte project, you can access it directly, e.g. with
- `Papa.parse('http://localhost:5000/beers.csv', { ... })`, or
- `fetch('http://localhost:5000/beers.json')`

## Recreating the flights visualisation
We now have the very basic components to use svelte for data visualisation. Let's use that to recreate the flights visualisation that we use in the other tutorials. This is what we'll be building:

<img src="{{ site.baseurl }}/assets/svelte-flights.png" width=600 />

In this visualisation, we see departure airports worldwide. The size of the dot is bigger is the flights are longer distance. Blue dots denote domestic flights; red dots are international flights. With the slider at the top we can filter on flight distance: with the slider at the left we only show short-distance flights; with the slider on the right we only show long-distance flights.

### Loading the data
The data for this visualisation is available at `http://vda-lab.github.io/assets/svelte-flights.json`. However, there are 57,852 records in that file which is too much to visualise using SVG. We'd be generating that many `circle` elements in the DOM. That's why we'll use only the first 3,000 records in that file.

We can check we're loading the file correctly by just creating a list of the departure airport names:
{% highlight html %}
<script>
  let datapoints = []
  fetch("http://vda-lab.github.io/assets/svelte-flights.json")
    .then(res => res.json())
    .then(data => datapoints = data.slice(1,3000))
</script>

<ul>
  {#each datapoints as datapoint}
    <li>{datapoint.from_airport} to {datapoint.to_airport}</li>
  {/each}
</ul>
{% endhighlight %}

This should give you the list:
- Balandino to Kazan
- Balandino to Tolmachevo
- Domododevo to Balandino
- Domododevo to Khrabrovo
- Domododevo to Kazan
- ...

### First attempt at plotting
The dataset also contains the latitude and longitude of the departure airports, in the variables `from_lat` and `from_long`. If we plot these out as a scatterplot we should get the map of the world. We replace the `ul` in the example above with an `svg` and add a circle for each datapoint. We'll also add some style to make sure that we know where the boundaries of the SVG are, and if there is an overlap between datapoints.

{% highlight html %}
<script>
  let datapoints = []
  fetch("http://vda-lab.github.io/assets/svelte-flights.json")
    .then(res => res.json())
    .then(data => datapoints = data.slice(1,3000))
</script>

<style>
  svg {
    background-color: whitesmoke;
  }
  circle {
    opacity: 0.3;
  }
</style>

<svg width=800 height=400>
  {#each datapoints as datapoint}
    <circle cx={datapoint.from_long} cy={datapoint.from_lat} r=3 />
  {/each}
</svg>
{% endhighlight %}

This is the result:

<img src="{{ site.baseurl }}/assets/svelte-vis1.png" width=400 />

...which is completely different from what we expected.

Actually this is logical: the values for longitude in the file range from -180 to +180, and those for latitude from -90 to +90. On the other hand, the range of pixels that we should use are from 0 to 800 for longitude and from 0 to 400 for latitude. So not only is everything compressed in one corner, but 3/4 of the points are even outside of the picture.

So we will have to rescale these values.

### Rescaling longitude and latitude
Instead of using `cx={datapoint.from_long}` we have to rescale that longitude from its original range (called its _domain_) to a new _range_. The formula to do this is:

$$\frac{(range_{max} - range_{min})*(x-domain_{min})}{domain_{max}-domain_{min}} + range_{min}$$

Let's put that in a function that we can use. Add the `rescale` function to the `script` section of your svelte file, and call it where we need to set `cx` and `cy`.
{% highlight javascript linenos %}
<script>
  let datapoints = []
  fetch("http://vda-lab.github.io/assets/svelte-flights.json")
    .then(res => res.json())
    .then(data => datapoints = data.slice(1,5000))

  const rescale = function(x, domain_min, domain_max, range_min, range_max) {
    return ((range_max - range_min)*(x-domain_min))/(domain_max-domain_min) + range_min
  }
</script>

<style>
  svg {
    background-color: whitesmoke;
  }
  circle {
    opacity: 0.3;
  }
</style>

<svg width=800 height=400>
  {#each datapoints as datapoint}
    <circle cx={rescale(datapoint.from_long, -180, 180, 0, 800)}
            cy={rescale(datapoint.from_lat, -90, 90, 0, 400)}
            r=3 />
  {/each}
</svg>{% endhighlight %}

The new function is defined on lines 7 to 9 and used in lines 23 and 24.

Our new image:

<img src="{{ site.baseurl }}/assets/svelte-vis2.png" width=400 />

This is better, but the world is upside down. This is because the origin [0,0] in SVG is in the top left, not the bottom left. We therefore have to flip the scale as well, and set the range to `400,0` instead of `0,400` for `cy`. If we do that we'll get the world the right side up.

### Scaling the size of the circles
We also want to scale the size of the circles: small for short distance flights, and big for long distance flights. To do this we'll need the minimum and maximum distance in the file, and can find out that this is 1 km and 15406 km. Let's set the minimum radius of a circle to 2 pixels and the maximum to 10 pixels. This is our new file (remember the switch from `0,400` to `400,0` from above):

{% highlight html %}
<script>
  let datapoints = []
  fetch("http://vda-lab.github.io/assets/svelte-flights.json")
    .then(res => res.json())
    .then(data => datapoints = data.slice(1,5000))

  const rescale = function(x, domain_min, domain_max, range_min, range_max) {
    return ((range_max - range_min)*(x-domain_min))/(domain_max-domain_min) + range_min
  }
</script>

<style>
  svg {
    background-color: whitesmoke;
  }
  circle {
    opacity: 0.3;
  }
</style>

<svg width=800 height=400>
  {#each datapoints as datapoint}
    <circle cx={rescale(datapoint.from_long, -180, 180, 0, 800)}
            cy={rescale(datapoint.from_lat, -90, 90, 400, 0)}
            r={rescale(datapoint.distance, 1, 15406, 2, 10)} />
  {/each}
</svg>
{% endhighlight %}

Our new image:

<img src="{{ site.baseurl }}/assets/svelte-vis3.png" width=400 />

### HTML class: setting the colour
Next, we want domestic flights to be blue and international flights to be red. We can do this because each flight has a `from_country` and a `to_country`. If these are the same we have a domestic flight, otherwise it is international. Here's we'll have to start using _classes_ and CSS selectors (see above). We can for example set the default colour of the circles to blue, but give those flights that are international the class attribute of `international`. We can then use that class attribute in the CSS to set the colour to red.

Let's first do the styling bit:
{% highlight html %}
<style>
  svg {
    background-color: whitesmoke;
  }
  circle {
    opacity: 0.3;
    fill: steelblue;
  }
  circle.international {
    fill: red;
  }
</style>
{% endhighlight %}

This will set the default color of circles to blue, except when they have the `international` class.

We'll have to do that programmatically in some way. A single `circle` element could look like this:

{% highlight html %}
<circle cx=500 cy=238 r=12 />
{% endhighlight %}

or

{% highlight html %}
<circle cx=500 cy=238 r=12 class="international" />
{% endhighlight %}

To add this, we will use an inline javascript expression:

{% highlight html %}
<circle cx={...}
        cy={...}
        r={...}
        class:international={datapoint.from_country != datapoint.to_country} />
{% endhighlight %}

Our final code looks like this:

{% highlight html %}
<script>
  let datapoints = []
  fetch("http://vda-lab.github.io/assets/svelte-flights.json")
    .then(res => res.json())
    .then(data => datapoints = data.slice(1,5000))

  const rescale = function(x, domain_min, domain_max, range_min, range_max) {
    return ((range_max - range_min)*(x-domain_min))/(domain_max-domain_min) + range_min
  }
</script>

<style>
  svg {
    background-color: whitesmoke;
  }
  circle {
    opacity: 0.3;
    fill: steelblue;
  }
  circle.international {
    fill: red;
  }
</style>

<svg width=800 height=400>
  {#each datapoints as datapoint}
    <circle cx={rescale(datapoint.from_long, -180, 180, 0, 800)}
            cy={rescale(datapoint.from_lat, -90, 90, 400, 0)}
            r={rescale(datapoint.distance, 1, 15406, 2, 10)}
            class:international={datapoint.from_country != datapoint.to_country} />
  {/each}
</svg>
{% endhighlight %}

Which gives the following (final) image:

<img src="{{ site.baseurl }}/assets/svelte-vis4.png" width=400 />

### Making the plot interactive with a slider
Let's add an additional feature to the plot. We want to add a slider to filter the airports that are shown on the screen. As svelte is regular HTML, we can easily make use of all HTML elements, and there appears to be one for a slider.

{% highlight html %}
<input type="range" min="1" max="15406" value="5000">
{% endhighlight %}

There is an extensive list of `input` element types, including color picker, button, radio button, password field, etc. But also `range` which represents a slider. In the code snippet above, we set the minimum value to 1, the maximum value to 15,406 and the default value to 5,000.

#### The filtering itself
Let's use an additional class on the circles: `hidden`. Circles should be hidden _unless_ their value for `distance` is less than 1,000 km difference from what is selected with the slider. So if the slider is at 5,000, all flights that are either less than 4,000 or more than 6,000 km should be hidden. It's good to first define the style. So add the following which will make the "hidden" circles not completely disappear, but makes them very transparent.

{% highlight html %}
circle.hidden {
  opacity: 0.05;
}
{% endhighlight %}

We can do the same as we did with international vs domestic flights: `class:hidden={compare distance to slider value here}`. But how can we access the value of the slider? We can define it in the `script` section. For example:

{% highlight html %}
<script>
  let slider_value = 5000;
</script>

<input type="range" min="1" max="15406" value={slider_value}

<svg>
    ...
    class:hidden="{Math.abs(datapoint.distance - slider_value) > 1000}">
</svg>
{% endhighlight %}

The full code looks like this:

{% highlight html %}
<script>
  let slider_value = 5000;

  let datapoints = []
  fetch("http://vda-lab.github.io/assets/svelte-flights.json")
    .then(res => res.json())
    .then(data => datapoints = data.slice(1,5000))

  const rescale = function(x, domain_min, domain_max, range_min, range_max) {
    return ((range_max - range_min)*(x-domain_min))/(domain_max-domain_min) + range_min
  }
</script>

<style>
  circle {
    opacity: 0.5;
    fill: blue;
  }
  circle.international {
    fill: red;
  }
  circle.hidden {
    opacity: 0.05;
  }
</style>

<h1>Airport flights data</h1>
Airports serving flights in this range (km): {slider_value - 1000} - {slider_value + 1000} <br/>
<input type="range" min="1" max="15406" bind:value={slider_value} class="slider" id="myRange" />
<svg width=1000 height=500>
  {#each datapoints as datapoint}
    <circle cx={rescale(datapoint.from_long, -180, 180, 0, 800)}
            cy={rescale(datapoint.from_lat, -90, 90, 400, 0)}
            r={rescale(datapoint.distance, 1, 15406, 2,10)}
            class:international="{datapoint.from_country != datapoint.to_country}"
            class:hidden="{Math.abs(datapoint.distance - slider_value) > 1000}">
      <title>{datapoint.from_airport}</title>
    </circle>
  {/each}
</svg>
{% endhighlight %}

This gives our final interactive tool:

<img src="{{ site.baseurl }}/assets/svelte-vis5.png" width=400 />

## Quick exercise: lines
See if you can adapt the previous script to generate the following image where departure airports are linked to their arrival airports.

<img src="{{ site.baseurl }}/assets/svelte-vis6.png" width=400 />
