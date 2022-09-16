
from django import forms


class editprofile(forms.Form):
    name = forms.CharField(required=False)
    role = forms.ChoiceField(choices=[('',""),(
        "Farmer", "Farmer"), ("Vendor", "Vendor"), ("Expert", "Expert"), ("Admin", "Admin")],required=False)
    bio = forms.CharField(max_length=255,required=False)

class money(forms.Form):
    amount = forms.FloatField(min_value=1,required=True)