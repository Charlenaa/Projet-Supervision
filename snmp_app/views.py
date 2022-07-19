from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

# Vue pour l'index : equipments
def equipments_list(request):
    html_template = loader.get_template('equipments.html')
    context = {'equipments': ['Equipement 1', 'Equipement 2', 'Equipement 3']}
    return HttpResponse(html_template.render(context, request))

# Vue pour la Table de Commutation
def tables_list(request):
    html_template = loader.get_template('tables.html')
    context = {'tables': ['Table 1', 'Table 2', 'Table 3']}
    return HttpResponse(html_template.render(context, request))

# Vue pour les Alertes
def alerts_page(request):
    html_template = loader.get_template('alerts.html')
    context = {'alerts': ['Alert 1', 'Alert 2', 'Alert 3']}
    return HttpResponse(html_template.render(context, request))
