from django import forms
from .models import Stuff
from .models import Review
from .models import Comment
from django.conf import settings


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
	
	
class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Stuff
        fields = ['name', 'photo']
		


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewtext', 'photo']
		
		
class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['commenttext', 'photo']