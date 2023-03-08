---
layout: default
category: "gamebooks"
---
{% assign series_books = site.categories['gamebooks'] | sort: "index" | where: "type", page.type %}

{% for post in series_books %}

  <a href="{{ post.url }}" title="{{ post.title }}">
    
    {% if post.year == "unread" %}
      <div class="fadelink">
    {% else %}
      <div class="divlink">
    {% endif %}
      {{ post.index }}. {{ post.title }}
    </div>
  </a>
 
{% endfor %}
