---
layout: default
---

{% assign postsBySeries = site.categories[page.category] | group_by_exp:"series" | sort:"year" %}
<div class="row">   
  {% for series in postsBySeries %}	
  <a href="/{{ page.category }}/{{ series.name  }}.html" title="{{ series.name }}">
    <div class="wrap">
      {{ series.name }}
    </div>
  </a>
 {% endfor %}
</div>
