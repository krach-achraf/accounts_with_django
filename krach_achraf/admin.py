from django.contrib import admin
from .models import Client, Compte, Operation


@admin.register(Client)
class Client(admin.ModelAdmin):
    pass


@admin.register(Compte)
class Compte(admin.ModelAdmin):
    pass


@admin.register(Operation)
class Operation(admin.ModelAdmin):
    pass
