---
title: Lecture sessions
layout: page
---
<ul>
  {% for post in site.categories.i0u19a reversed %}
  {% unless post.instructor %}
    <li>
      <time style="color:#666;font-size:11px;" datetime='{{post.date | date: "%Y-%m-%d"}}'>{{post.date | date: "%m/%d/%y"}}</time> <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endunless %}
  {% endfor %}
</ul>
