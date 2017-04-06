---
layout: page
title: People
menu: main
navigation_weight: 2
color: "#b3e2cd"
---
## Current lab members

{% for person in site.data.people %}
{% if person.class == 'current' %}
<img src="{{site.baseurl}}/assets/{{person.image}}"/><br/>
<b>{{person.name}}</b><br/>
{{person.title}}<br/>{% if person.orcid %}
<a href="{{person.orcid}}"><img src="{{site.baseurl}}/assets/orcid_24x24.gif" /></a>
{% endif %}<a href="mailto:{{person.email}}"><img src="{{site.baseurl}}/assets/ic_email_black_24dp_1x.png" /></a>{% if person.twitter %}
<a href="http://www.twitter.com/{{person.twitter}}"><img src="{{site.baseurl}}/assets/twitter-logo.png" /></a>
{% endif %}{% if person.website %}
<a href="{{person.website}}"><img src="{{site.baseurl}}/assets/ic_link_black_24dp_1x.png" /></a>
{% endif %}<br/>
{{person.bio}}<br/>
<br/>
{% endif %}
{% endfor %}

## Alumni
{% for person in site.data.people %}
{% if person.class == 'alumnus' %}
<img src="{{site.baseurl}}/assets/{{person.image}}"/><br/>
<b>{{person.name}}</b><br/>
{{person.title}}<br/>{% if person.orcid %}<a href="{{person.orcid}}"><img src="{{site.baseurl}}/assets/orcid_24x24.gif" /></a>{% endif %}{% if person.twitter %}<a href="http://www.twitter.com/{{person.twitter}}"><img src="{{site.baseurl}}/assets/twitter-logo.png" /></a>{% endif %}{% if person.website %}<a href="{{person.website}}"><img src="{{site.baseurl}}/assets/ic_link_black_24dp_1x.png" /></a>{% endif %}{% if person.bio %}<br/>{{person.bio}}{% endif %}<br/>
<br/>
{% endif %}
{% endfor %}

## Visitors
{% for person in site.data.people %}
{% if person.class == 'visitor' %}
<img src="{{site.baseurl}}/assets/{{person.image}}"/><br/>
<b>{{person.name}}</b><br/>
{{person.title}}{% if person.bio %}<br/>{{person.bio}}{% endif %}<br/>
{% endif %}
{% endfor %}

## MSc thesis students

{% for person in site.data.people %}
{% if person.class == 'student' %}
{{person.year}}: <b>{{person.name}}</b> ({{person.master}}) - {{person.topic}}
{% endif %}
{% endfor %}
