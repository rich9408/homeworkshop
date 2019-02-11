문제 1

    {% for comment in question.comment_set.all %}
        <h3>{{comment.content}}</h3>
    {% endfor %}
    
문제 2
 <form action="/questions/{{question.pk}}/comment/create/" method="post">
