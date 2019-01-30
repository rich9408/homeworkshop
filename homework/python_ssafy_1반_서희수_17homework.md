문제 1
migration

문제 2
max_length=100

문제 3
python manage.py shell


문제 4
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()