---
permalink: /
author_profile: true
---
{% include base_path %}

<h1>Bio Notes</h1>
{{site.author.description}}

## News
<a href="{{ site.url }}{{ site.baseurl }}/news/">(Complete list)</a>
<ul style="list-style-type: none; padding-left: 0;">
  {% assign sorted_news = site.data.news.news | sort: "date" | reverse %}
  {% for item in sorted_news limit:10 %}
    <li>
      <strong>{{ item.date }}</strong> -
      {{ item.title }}
      {% if item.venue %}
        at <em>{{ item.venue }}</em>
      {% endif %}
      {% if item.award %}
        ({{ item.award }})
      {% endif %}
      {% if item.links %}
        {% for link in item.links %}
          {% for key in link %}
            (<a href="{{ link[key] }}" target="_blank">{{ key }}</a>)
          {% endfor %}
        {% endfor %}
      {% endif %}
      {% if item.locations %}
        at {{ item.locations | join: ', ' }}
      {% endif %}
    </li>
  {% endfor %}
</ul>

## Recent Activities 
<a href="{{ site.url }}{{ site.baseurl }}/activities/">(Complete list)</a>
<ul>
<li>Associate Editor:

  {% assign ae_items = site.data.activities.pc_member | where_exp: "item", "item.role == 'Associate Editor'" %}
  {% assign ae_by_venue = {} %}

  {% for item in ae_items %}
    {% for conf in item.conferences %}
      {% assign venue = conf.name %}
      {% assign years = conf.years %}
      {% assign existing = ae_by_venue[venue] | default: "" %}
      {% assign ae_by_venue = ae_by_venue | merge: {{ venue | jsonify }}: existing | append: years %}
    {% endfor %}
  {% endfor %}

  {% comment %} Custom render associate editor as string {% endcomment %}
  {% assign ae_output = "" %}
  {% for conf in site.data.activities.associate_editor %}
    {% assign name = conf.journal | default: conf.conference %}
    {% if conf.since %}
      {% assign display_years = "since " | append: conf.since %}
    {% else %}
      {% assign display_years = conf.years | join: ", " %}
    {% endif %}
    {% assign ae_output = ae_output | append: name | append: " (" | append: display_years | append: "), " %}
  {% endfor %}
  {{ ae_output | strip | strip_newlines | remove_last: ", " }}
</li>

<li>PC Member:
  {% assign pc_output = "" %}
  {% for year_item in site.data.activities.pc_member %}
    {% assign year = year_item.year %}
    {% assign confs = year_item.conferences | join: ", " %}
    {% assign pc_output = pc_output | append: confs | append: " (" | append: year | append: "), " %}
  {% endfor %}
  {{ pc_output | strip | strip_newlines | remove_last: ", " }}
</li>
</ul>

## Selected Publications
{% for category in site.data.research.categorys %}
  <h3>{{ category.title }}</h3>
  <ul>
    {% assign papers_in_category = site.data.research.research | where: "category", category.name | sort: "year" | reverse %}
    {% for paper in papers_in_category %}
      <li>
        <strong>({{ paper.year }}) {{ paper.title }}</strong><br>
        <em>{{ paper.authors }}</em><br>
        <span>In {{ paper.publication }}</span>
      </li>
    {% endfor %}
  </ul>
{% endfor %}
