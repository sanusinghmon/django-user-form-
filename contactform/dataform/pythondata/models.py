from django.db import models
from django.forms import ModelForm

class userinsert (models.Model):
      id = models.AutoField(primary_key=True)
      username = models.CharField (max_length=100)
      email = models.CharField(max_length=100)

def __str__(self):
        return "%s %s" % (self.username, self.email)