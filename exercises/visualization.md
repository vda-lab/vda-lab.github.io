# Visualisation #

## Assignment to be performed before the exercise session ##

For the visualization exercises, we will use the [paper.js](http://paperjs.org) library. Paper.js is based on javascript, so you should become acquainted with that language.

The following links can help in preparing:

* Follow the Javascript course on [Codecademy](http://www.codecademy.com/tracks/javascript).
* Have a look at the tutorials and reference material on [paper.js](http://paperjs.org).

The preparation assignment consists of two parts.

### Part 1: Bad data visualization example

Search literature and/or the internet to find an example of bad data visualization. **Upload the picture to Toledo.**

### Part 2: Paper.js implementation

Get acquainted with paper.js - paper.js is a data visualization library to create custom data visualizations.

The following code displays a scatterplot using paper.js:

```
var data = [
    {x:345,y:30,z:445,colour:"green",size:4},
    {x:475,y:305,z:390,colour:"blue",size:16},
    {x:430,y:50,z:305,colour:"green",size:2},
    {x:85,y:295,z:260,colour:"yellow",size:14},
    {x:465,y:120,z:460,colour:"red",size:2},
    {x:105,y:110,z:190,colour:"blue",size:6},
    {x:215,y:220,z:325,colour:"red",size:16},
    {x:480,y:430,z:415,colour:"red",size:10},
    {x:105,y:210,z:35,colour:"blue",size:22},
    {x:415,y:475,z:15,colour:"green",size:16}
]

// Draw the axes
var yAxis = new Path.Line(new Point(10,10), new Point(10,500))
yAxis.strokeColor = 'black'
var xAxis = new Path.Line(new Point(10,500), new Point(500,500))
xAxis.strokeColor = 'black'

// Draw the datapoints
for ( var i = 0; i < data.length; i++ ) {
    var size = 5
    var circle = new Path.Circle(new Point(data[i].x, data[i].y), size)
    circle.fillColor = data[i].colour
}
```

You can use [sketch.paperjs.org](http://sketch.paperjs.org) to check if it works and to make some simple changes: changing the color and size of the dots.

Replace the code in the `visualization/simple.js` file in your home directory on the server with the code that you wrote in sketch.paperjs.org, so that we can have a look at it during the exercise session itself. 

You can see if it works [by going to](visualization/index.html) 

    http://50.16.33.38:8000/exercises/visualization

and clicking on your username. A template file has been provided in (a subdirectory of) your home directory on the teaching server. It can be found here:

    ~/visualization/simple.js

If this works, modify the code such that it draws a _parallel coordinate_ plot of the _3 dimensions_ in the data provided. **Update the version on the server with your new parallel coordinate version.** This will be checked the morning of the exercise session.


## Exercise Session ##

During the exercise session, you will be given a visualization. In groups, you will discuss what aspects of this visualization are good and bad and come up with possible improvements.

Each group will then present its analysis.
