from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("name","email","body")


class AgriCommentForm(forms.ModelForm):
    
    class Meta:
        model = AgriComment
        fields = ("name","email","body")


class MarketCreate(forms.ModelForm):
    class Meta:
        models = MarketPost
        fields = ['type_of_item','description','contact','image']
