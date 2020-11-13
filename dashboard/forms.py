from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Blog


class BlogForm(ModelForm):
	class Meta:
		model = Blog
		fields = '__all__'
		widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control', }),
				'description': forms.TextInput(attrs={'class': 'form-control', }),
				'content': forms.TextInput(attrs={'class': 'form-control', }),
				'slug': forms.TextInput(attrs={'class': 'form-control', }),
			}
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = [ 'username', 'email', 'password1', 'password2']
		widgets = {
                'username': forms.TextInput(attrs={'class': 'form-control', }),
				'email': forms.TextInput(attrs={'class': 'form-control', }),
				'password1': forms.TextInput(attrs={'class': 'form-control', }),
				'password2': forms.TextInput(attrs={'class': 'form-control', }),
			}
