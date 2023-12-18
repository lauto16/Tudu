from django import forms

class Login(forms.Form):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(label="", max_length=100, widget=forms.PasswordInput(attrs={'placeholder': "Contraseña"}))


class Register(forms.Form):
    nombre = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    email = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="", max_length=30, widget=forms.PasswordInput(attrs={'placeholder': "Contraseña"}))
    password_repeat = forms.CharField(label="", max_length=30, widget=forms.PasswordInput(attrs={'placeholder': "Repetir contraseña"}))

class Note(forms.Form):
    title = forms.CharField(required=True, label="", max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Titulo de la nota'}))
    note = forms.CharField(required=False, label="", max_length=1624, widget=forms.Textarea(attrs={'placeholder': 'Escriba su nota aqui...'}))
   