from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User

class SignIn(AuthenticationForm):
    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class':'form-control'}))
    password= forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))

class PromoCodeRegistration(forms.Form):
    code = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))

class PlayerStickerRegistration(forms.Form):
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    country = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    position =forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))

class UserRegistration(UserCreationForm):
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    country = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1= forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='Repita la contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','username','password1','password2']
        help_texts = {k:"" for k in fields}