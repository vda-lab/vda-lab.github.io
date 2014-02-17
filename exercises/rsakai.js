var data = [
  {x:50,y:190,radius:4},
  {x:130,y:130,radius:10},
  {x:90,y:110,radius:6}
]

for ( var i = 0; i < data.length; i++ ) {
  var circle = new Path.Circle(new Point(data[i].x, data[i].y),data[i].radius)
  circle.fillColor = 'blue'
}
