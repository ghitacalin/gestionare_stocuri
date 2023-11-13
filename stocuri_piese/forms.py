from django import forms 

class CautaPiesaForm(forms.Form):
    model_input = forms.CharField(label="Introduceti modelul", widget=forms.TextInput(attrs={"placeholder": "Introduceti modelul", "style": "height: 31px;"}))

class CautaModelForm(forms.Form):
    cod_piesa_input = forms.CharField(label="Intorduceti codul piesei", widget=forms.TextInput(attrs={"placeholder": "Introduceti codul piesei", "style": "height: 31px;"}))