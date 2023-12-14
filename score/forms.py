from django import forms

class PDMScoreForm(forms.Form):
    w1 = forms.FloatField()
    w2 = forms.FloatField()
    w3 = forms.FloatField()
    nsr = forms.FloatField()
    rb = forms.FloatField()
    sensitivity = forms.FloatField()