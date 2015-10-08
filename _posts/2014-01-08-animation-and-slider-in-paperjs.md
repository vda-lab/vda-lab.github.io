---
layout: post
title:  "Animation and slider in paper.js"
date:   2014-01-08 11:00:00
author: Jan Aerts
categories: paperjs howto
---
![Animation and slider paper.js]({{ site.baseurl }}/assets/animation_and_slider_paperjs.png)

One of the issues with processing.org is the way that it handles sliders in a sketch. In contrast to D3, the developer has to either check himself if the mouse position is within the pixel range of a slider glyph, or use external libraries. Although paper.js uses canvas rather than SVG (as D3 does), it allows for linking events to objects. This makes it much easier to create e.g. sliders. In the code below, I combine a slider with an animated object. The position of the slider determines the speed at which the animated object moves across the screen. As it only checks the speed when it changes direction, any change in the slider setting will only take place at that point.

{% highlight javascript %}
function rescale(valueFrom, minFrom, maxFrom, minTo, maxTo) {
    return (valueFrom - minFrom) * ((maxTo - minTo)/(maxFrom - minFrom)) + minTo
}

// Blue circle
var circle = new Path.Circle({
    x:200,
    y:300,
    radius: 20,
    fillColor: "blue"})

// Grey bar
var bar = new Path();
bar.add(new Point(300,400));
bar.add(new Point(500,400));
bar.strokeColor = 'lightgrey';
bar.strokeWidth = 20;

// Black circle on bar
var marker = new Path.Circle({
    x:300,
    y:400,
    radius: 5,
    fillColor: "black"})

// This is where the magic happens
var stepSize = 1;
function onMouseDrag(event) {
    var hitResult = bar.hitTest(event.point, {stroke: true, tolerance: 0});
    if (hitResult) {
        stepSize = rescale(event.point.x,300,500,1,20);
        marker.position.x = event.point.x;
    }
}

function onFrame(event) {
    if ( circle.position.y &gt;= 700 ) {
        movement = -1 * stepSize
    } else if ( circle.position.y &lt;= 300 ) {
        movement = stepSize
    }
    circle.position.y += movement
}
{% endhighlight %}

As yokofakun would say: "That is all".

 [1]: https://securehomes.esat.kuleuven.be/~bioiuser/blog/wp-content/uploads/2014/01/Screen-Shot-2014-01-08-at-12.56.27.png
