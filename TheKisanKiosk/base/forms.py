from django import forms
from .models import Credentials


class credentialsreg(forms.ModelForm):
    class Meta:
        model = Credentials
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput,
            'username': forms.TextInput(attrs={'autofocus': True})
        }
