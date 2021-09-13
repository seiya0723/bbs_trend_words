from django import forms
from .models import Topic,Trend

class TopicForm(forms.ModelForm):

    class Meta:
        model   = Topic
        fields  = [ "comment" ]

class TrendForm(forms.ModelForm):

    class Meta:
        model   = Trend
        fields  = [ "word","count" ]



