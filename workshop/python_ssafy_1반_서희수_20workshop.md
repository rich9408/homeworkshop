
class Question(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
        
class Choice(models.Model):
    content = models.CharField(max_length=50)
    votes = models.IntegerField()
    def __str__(self):
        return self.content




