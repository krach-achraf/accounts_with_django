from django import forms
from .models import Client, Compte, Operation


class ClientForm(forms.Form):
    code = forms.CharField()
    nom = forms.CharField()
    prenom = forms.CharField()


class CompteForm(forms.Form):
    numero = forms.CharField()
    date_creation = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    solde = forms.DecimalField()
    client = forms.ModelChoiceField(queryset=Client.objects.all(), initial=0)

    class Meta:
        model = Client
        fields = [
            "code", "nom", "prenom"
        ]


class OperationForm(forms.Form):
    types = (('versement', 'versement'), ('retrait', 'retrait'))
    numero = forms.CharField()
    date_operation = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    montant = forms.DecimalField()
    type = forms.ChoiceField(choices=types, widget=forms.RadioSelect)
    compte = forms.ModelChoiceField(queryset=Compte.objects.all(), initial=0)

    class Meta:
        model = Compte
        fiels = [
            "num", "dateCreation", "solde", "client"
        ]