

from django import forms
from django import forms
from base.models import *


class profilereg(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'role']
