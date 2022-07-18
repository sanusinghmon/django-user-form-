from django.forms import fields
from django import forms
from .models import userinsert

class userinsert (forms.ModelForms):

    class meta:
       model=userinsert
       fields = '__all__'
