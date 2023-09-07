---
layout: page
title: Publications
menu: main
navigation_weight: 6
color: "#e6f5c9"
---
<ul style="list-style-type: none;">
{% for publication in site.data.publications %}
  <li>
    {{ publication.authors }}<br/>
    <b>{{publication.title}}</b><br/>
    {{publication.reference}} ({{publication.year}})<br/>
    {% if publication.pdf %}
    <a href="{{ site.baseurl}}/assets/{{publication.pdf}}"><img src="{{ site.baseurl }}/assets/ic_picture_as_pdf_black_24dp_1x.png"/></a>
    {% endif %}
    {% if publication.url %}
    <a href="{{publication.url}}"><img src="{{ site.baseurl }}/assets/ic_link_black_24dp_1x.png"/></a>
    {% endif %}
    {% if publication.doi %}
    <a href="http://doi.org/{{publication.doi}}"><img src="{{ site.baseurl }}/assets/ic_link_black_24dp_1x.png"/></a>
    {% endif %}
    {% if publication.app %}
    <a href="{{publication.app}}"><img src="{{ site.baseurl }}/assets/ic_launch_black_24dp_1x.png"/></a>
    {% endif %}

  </li>
  <br/>
{% endfor %}
</ul>