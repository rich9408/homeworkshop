문제 1
class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    
    def __str__(self):
        return self.content
        
        
문제 2

def comment_create(request,id):
    question = Question.objects.get(pk=id)
    content = request.POST.get("content")
    
    Comment.objects.create(question=question,content=content)
    return redirect(f"/questions/{id}/")
    

문제 3
movie.id
