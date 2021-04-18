from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_contact),
    path('create', views.create_contact),
]
