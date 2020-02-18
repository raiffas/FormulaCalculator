

## Formula Calculator
CS 499 Project for Delta V Innovations

  <ul class="post-list">
    {% for post in site.posts %}
    {% if post.Honor != null %}
        <li>
        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>

        <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>

      </li>
    {% endif %}
    {% endfor %}
  </ul>

  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | relative_url }}">via RSS</a></p>
