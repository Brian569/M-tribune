from .models import Article, Profile
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class UserForm(forms.ModelForm):
    model = Profile
    username = forms.CharField(label='Username', max_length=30)
    bio = forms.CharField(label='Bio', max_length=500)
    profile_pic = CloudinaryField()

class ProfileUpload(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']