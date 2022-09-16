from base.models import Post
from django import forms


class post(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(),
            'title': forms.TextInput(attrs={'autofocus': True})
        }