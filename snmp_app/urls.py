"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from snmp_app import views
"""
- Avoir la liste de tous les équipements connectés sur le réseau et leur adresse MAC
- Afficher la table de commutation
- Remonter les alertes en cas de panne 
"""

urlpatterns = [
    path('', views.equipments_list, name='index'),
    path('equipments/', views.equipments_list, name = 'equipments'),
    # path('/equipments/<int:equipment_id>/', views.equipment_detail, name = 'equipment_detail'),
    path('tables/', views.tables_list, name = 'tables'),
    path('alerts/', views.alerts_page, name = 'alerts'),
]
