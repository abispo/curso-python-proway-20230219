from django import forms

class PreRegistroForm(forms.Form):
    email = forms.EmailField(required=True, label="E-mail", widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Informe o seu E-mail"}))