# Jekyll code for VDA-lab website

## Making changes

The changes have to be uploaded to the ESAT webserver, because jekyll is not installed there. This means that we had to set the base_url variable in `_config.yml` to `~jaerts`

After making changes locally:

* `jekyll build`
* `tar -cvzf _site vda-lab.tar.gz`
* `scp vda-lab.tar.gz ssh.esat.kuleuven.be:/users/stadius/jaerts/`

On the server:

* `tar -xvzf vda-lab.tar.gz`
* `rm -r -f public_html`
* `mv _site public_html`

## To get tags visual using P5
```
<div id="visual"></div>
<script type="text/javascript" src="p5.min.js"></script>
<script>
var alltags

function setup() {
  {% capture posts %}
  [
  {% for post in site.posts %}
  {
  "title"    : "{{ post.title }}",
  "url"      : "{{ post.url }}",
  "date"     : "{{ post.date | date: "%B %d, %Y" }}",
  "tags"     : "{{ post.tags | join: ';' }}"
  } {% if forloop.last %}{% else %},{% endif %}
  {% endfor %}
  ]
  {% endcapture %}
  var posts = {{posts | strip_newlines}}
  posts.map(function(p) {
    p.tags = p.tags.split(';')
  })
  console.log(posts)

  alltags = posts.map(function(p) {
    return p.tags.map(function(t) {
      return {"tag": t, "url": p.url}
    })
  }).reduce(function(prev,curr) {
    return prev.concat(curr) // [{tag:'paperjs', title:'url1'}, {tag:'howto', title:'url2'}, {tag:'paperjs',title:'url3'}]
  }).reduce(function(prev, curr) {
    var newObject = prev
    if ( ! newObject[curr['tag']] ) {
      newObject[curr['tag']] = []
    }
    newObject[curr['tag']].push(curr['url'])
    return newObject
  },{}) // {polymer:[url1,url2],paperjs:[url3,url4,url5],d3:[url6],...}

  var myCanvas = createCanvas(800, 200);
  myCanvas.parent('visual')

  noLoop()
}

function draw() {
  var horizontalOffset = 0
  var verticalOffset = 10
  Object.keys(alltags).sort(function(a,b) {
    return alltags[b].length - alltags[a].length
  }).forEach(function(tag) {
    textSize(10*alltags[tag].length)
    text(tag, horizontalOffset, verticalOffset)
    horizontalOffset += textWidth(tag) + 10
    if ( horizontalOffset > 600 ) {
      horizontalOffset = 0
      verticalOffset += 20
    }

  })
}
</script>
```
