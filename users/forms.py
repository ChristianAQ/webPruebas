from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput())


class SignupForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput())
    pwd2 = forms.CharField(label="Repite contraseña", widget=forms.PasswordInput())

