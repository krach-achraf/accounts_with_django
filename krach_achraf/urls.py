from django.urls import path
from . import views

urlpatterns = [
    path('clients', views.get_clients, name='get_clients'),
    path('comptes', views.get_comptes, name='get_comptes'),
    path('details_client/<str:code>', views.details_client, name='details_client'),
    path('search_clients/<str:nom>', views.search_clients, name='search_clients'),
    path('operations_client/<str:code>', views.get_operations_client, name='get_operations_client'),
    path('add_client', views.add_client, name='add_client'),
    path('add_compte', views.add_compte, name='add_compte'),
    path('add_operation', views.add_operation, name='add_operation'),
    path('save_client', views.save_client, name='save_client'),
    path('save_compte', views.save_compte, name='save_compte'),
    path('save_operation', views.save_operation, name='save_operation'),
]
