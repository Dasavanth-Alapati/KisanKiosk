

from django import forms
from base.models import Listing

class listingform(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['name','description','price']
        widgets = {
            'description': forms.Textarea(),
            'name': forms.TextInput(attrs={'autofocus': True})
        }