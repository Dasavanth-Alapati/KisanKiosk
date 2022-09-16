from django import forms


class likedata(forms.Form):
    type = forms.CharField()
    id = forms.IntegerField()