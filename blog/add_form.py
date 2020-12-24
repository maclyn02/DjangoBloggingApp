from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.models import User

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Sign Up', 'Sign Up', css_class='btn btn-primary'))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
