"""ticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('grab_tickets', views.grab_tickets),
    path('show_order', views.show_order),
    path('add_ticket',views.add_ticket),
    path('show_ticket', views.show_ticket),
    path('delete_order',views.delete_order),
    path('show_self_order', views.show_self_order),
    path('lock_order', views.lock_order),
    path('search', views.search)
]
