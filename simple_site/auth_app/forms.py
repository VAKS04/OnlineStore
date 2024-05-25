from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label="Имя")
    password = forms.CharField(label="Пароль")
    password2 = forms.CharField(label="Повторите пароль")
    email = forms.EmailField(label= "Email")


    class Meta:
        model = get_user_model()
        fields = ['username','password','email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise forms.ValidationError("Пароли не совпали")
        return cd['password']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email = email).exists():
            raise forms.ValidationError("Пользователь с данным email уже существует")
        return email
    
    def clean_username(self):
        username = self.cleaned_data["username"]

        if get_user_model().objects.filter(username = username).exists():
            raise forms.ValidationError("Пользователь с таким именем уже суцествует")
        return username
    

class AuthUserForm(AuthenticationForm):
    username = forms.CharField(label="Имя")
    password = forms.CharField(label="Пароль")