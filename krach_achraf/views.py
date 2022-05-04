from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Client, Compte, Operation
from django.core import serializers
from django.core.paginator import Paginator
from .forms import ClientForm, CompteForm, OperationForm


def get_clients(request):
    clients = Client.objects.all()
    paginator = Paginator(clients, 4)  # change 4 to 10

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'listes/clients.html', {'page_obj': page_obj})


def get_comptes(request):
    comptes = Compte.objects.all()
    data = serializers.serialize('json', comptes)
    return HttpResponse(data, content_type="application/json")


def details_client(request, code):
    client = Client.objects.get(code=code)
    return render(request, 'details/client.html', {'client': client})


def search_clients(request, nom):
    clients = Client.objects.filter(nom__contains=nom)
    data = serializers.serialize('json', clients)
    return HttpResponse(data, content_type="application/json")


def get_operations_client(request, code):
    operations = Operation.objects.select_related('compte__client').filter(compte__client=code)
    return render(request, 'listes/operations.html', {'operations': operations})


def add_client(request):
    form = ClientForm()
    return render(request, 'forms/client.html', {'form': form})


def add_compte(request):
    form = CompteForm()
    return render(request, 'forms/compte.html', {'form': form})


def add_operation(request):
    form = OperationForm()
    return render(request, 'forms/operation.html', {'form': form})


def save_client(request):
    code = request.POST.get('code')
    nom = request.POST.get('nom')
    prenom = request.POST.get('prenom')
    client = Client.objects.create(code=code, nom=nom, prenom=prenom)
    client.save()
    return redirect("/controle/clients")


def save_compte(request):
    numero = request.POST.get('numero')
    dateCreation = request.POST.get('date_creation')
    solde = request.POST.get('solde')
    client = request.POST.get('client')
    compte = Compte.objects.create(num=numero, dateCreation=dateCreation, solde=solde, client_id=client)
    compte.save()
    return redirect("/controle/comptes")


def save_operation(request):
    numero = request.POST.get('numero')
    dateOperation = request.POST.get('date_operation')
    montant = request.POST.get('montant')
    typeOperation = request.POST.get('type')
    compte = request.POST.get('compte')
    operation = Operation.objects.create(numOperation=numero,
                                         dateOperation=dateOperation,
                                         typeOperation=typeOperation,
                                         montant=montant,
                                         compte_id=compte)
    operation.save()
    return redirect("/controle/add_operation")