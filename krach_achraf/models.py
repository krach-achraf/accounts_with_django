from django.db import models


class Client(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)

    def __str__(self):
        return self.code


class Compte(models.Model):
    num = models.CharField(max_length=16)
    dateCreation = models.DateField()
    solde = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.num


class Operation(models.Model):
    types = [
        ('versement', 'versement'),
        ('retrait', 'retrait')
    ]
    numOperation = models.IntegerField(primary_key=True)
    dateOperation = models.DateField()
    montant = models.DecimalField(max_digits=6, decimal_places=2)
    typeOperation = models.CharField(max_length=10, choices=types)
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE)

    def __str__(self):
        return self.numOperation