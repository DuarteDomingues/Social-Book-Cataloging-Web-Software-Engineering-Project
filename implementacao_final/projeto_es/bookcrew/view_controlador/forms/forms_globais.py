from django import forms

class FormBarra(forms.Form):
    casa = forms.CharField(widget=forms.HiddenInput())
    colecao = forms.CharField(widget=forms.HiddenInput())
    procura = forms.CharField(widget=forms.HiddenInput())
    perfil = forms.CharField(widget=forms.HiddenInput())




