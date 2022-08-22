from django.forms import ModelForm, TextInput, EmailInput,PasswordInput
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import teachers
from django import forms



class teachersForm(ModelForm):
    class Meta:
        model = teachers
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={ 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={  'style': 'width: 300px;', 'class': 'form-control'}))
    degree = forms.CharField(widget=forms.TextInput(attrs={ 'style': 'width: 300px;', 'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={ 'style': 'width: 300px;', 'class': 'form-control'}))
    password1: forms.CharField(widget=forms.PasswordInput(attrs={ 'style': 'width: 300px;', 'class': 'form-control'}))
    password1: forms.CharField(widget=forms.PasswordInput(attrs={ 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','degree','password1','password2','email','phone']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
            
            'degree':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                }),

            'password1':PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                }),
            'password2':PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                }),                     
                'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                }),
            'phone': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                }),
            
        }
                


