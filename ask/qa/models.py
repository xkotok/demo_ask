from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(default=datetime.datetime.now())
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='question_author',  null=True, 
                    on_delete=models.SET_NULL)
    like = models.ManyToManyField(User, related_name='question_like')
 
    def get_url(self):
        url = '/question/' + str(self.id) # bad hardcoded path
        return url
    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(default=datetime.datetime.now())
    question = models.ForeignKey(Question, 
                    on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, 
                    on_delete=models.SET_NULL)
    
