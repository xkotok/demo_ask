from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
#    rating = models.IntgerField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, related_name='question_author',  null=True, 
                    on_delete=models.SET_NULL)
    like = models.ManyToManyField(User, related_name='question_like')
    
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, 
                    on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, 
                    on_delete=models.SET_NULL)
    
    
