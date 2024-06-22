from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomerUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'Password'}),
    )

    class Meta:
        model = CustomerUser
        fields = ['username', 'email', 'mometary', 'type_user']
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control', 'type':'text', 'align':'center', 'placeholder':'User Name'}),
            'email':forms.TextInput(attrs={'class':'form-control', 'type':'text', 'align':'center', 'placeholder':'Email'}),
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.mometary = 0
        user.type_user = 'normal'
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )

    class Meta:
        model = CustomerUser
        fields = ['username', 'email', 'mometary', 'type_user']
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control', 'type':'text', 'align':'center', 'placeholder':'User Name'}),
            'email':forms.TextInput(attrs={'class':'form-control', 'type':'text', 'align':'center', 'placeholder':'Email'}),
        }