---
layout: page
title: Portfolio
menu: main
navigation_weight: 3
color: "#fdcdac"
---
A selection of projects, tools and designs developed in the lab…

## Visualization and design
<table>
{% for portfolio in site.data.portfolio %}
  {% if portfolio.class == "viz" %}
    <tr>
    <td><img src="{{site.baseurl}}/assets/{{portfolio.image}}" /></td>
    <td>
      <b>{{portfolio.title}}</b><br/>
      {{portfolio.description}}<br/>
      {% if portfolio.url %}
      <a href="{{portfolio.url}}"><img src="{{ site.baseurl }}/assets/ic_link_black_24dp_1x.png"/></a>
      {% endif %}
      {% if portfolio.video %}
      <a href="{{portfolio.video}}"><img src="{{ site.baseurl }}/assets/ic_video_library_black_24dp_1x.png"/></a>
      {% endif %}
    </td>
    </tr>
  {% endif %}
{% endfor %}
</table>

<p></p>

## Backend
<table>
{% for portfolio in site.data.portfolio %}
  {% if portfolio.class == "backend" %}
  <tr>
  <td><img src="{{site.baseurl}}/assets/{{portfolio.image}}" /></td>
  <td>
    <b>{{portfolio.title}}</b><br/>
    {{portfolio.description}}<br/>
    {% if portfolio.url %}
    <a href="{{portfolio.url}}"><img src="{{ site.baseurl }}/assets/ic_link_black_24dp_1x.png"/></a>
    {% endif %}
    {% if portfolio.video %}
    <a href="{{portfolio.video}}"><img src="{{ site.baseurl }}/assets/ic_video_library_black_24dp_1x.png"/></a>
    {% endif %}
  </td>
  </tr>
  {% endif %}
{% endfor %}
</table>

<p></p>

## HIV
<table>
{% for portfolio in site.data.portfolio %}
  {% if portfolio.class == "HIV" %}
  <tr>
  <td><img src="{{site.baseurl}}/assets/{{portfolio.image}}" /></td>
  <td>
    <b>{{portfolio.title}}</b><br/>
    {{portfolio.description}}<br/>
    {% if portfolio.url %}
    <a href="{{portfolio.url}}"><img src="{{ site.baseurl }}/assets/ic_link_black_24dp_1x.png"/></a>
    {% endif %}
    {% if portfolio.video %}
    <a href="{{portfolio.video}}"><img src="{{ site.baseurl }}/assets/ic_video_library_black_24dp_1x.png"/></a>
    {% endif %}
  </td>
  </tr>
  {% endif %}
{% endfor %}
</table>
