{{question.title}}

<ul>
    {% for choice in question.choice_set.all %}
        <li>{{choice.content}}:{{choice.votes}}표</li>
    {% endfor %}
    
</ul>