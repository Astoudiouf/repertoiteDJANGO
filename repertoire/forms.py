from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Nom d'utilisateur",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur", 'required': True, 'autofocus': True})
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe', 'required': True})
    )