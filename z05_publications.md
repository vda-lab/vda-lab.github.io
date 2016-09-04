---
layout: page
title: Publications
permalink: publications.html
menu: main
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
    {% if publication.app %}
    <a href="{{publication.app}}"><img src="{{ site.baseurl }}/assets/ic_launch_black_24dp_1x.png"/></a>
    {% endif %}

  </li>
  <br/>
{% endfor %}
</ul>

## :: General media ::

* De Standaard, 04/06/2014, “Je smartphone als dokter”
* Aerts J. Enhancing genomic analysis through ICT and visualisation. Projects, Insight Publishers, p28-31 (2013)
* Scheire, L. & Van Tendeloo, H. (2012) Wat cellen voorspellen: de genetica van de toekomst. Humo, 3725/04, 10-15
