from django.urls import path
from bonkers_app import views

urlpatterns = [
    path('', views.bonkers, name='bonkers_app'),
]