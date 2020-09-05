import random
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class TimeStampMixin(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Question(models.Model):

    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text=_("Enter the question text that "
                                           "you want displayed"),
                               verbose_name=_('Question'))

    option1=models.TextField(max_length=40,blank=True,null=True)
    option2=models.TextField(max_length=40,blank=True,null=True)
    option3=models.TextField(max_length=40,blank=True,null=True)
    option4=models.TextField(max_length=40,blank=True,null=True)




    def __str__(self):
        return self.content

class Answer(models.Model):
    qid = models.ForeignKey(Question,verbose_name='Question',on_delete=models.CASCADE)
    answer = models.TextField(max_length=40,blank=True,null=True,verbose_name="Correct Answer")

   


