from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items', views.model_item_list, name='items'),
    path('rules', views.rules, name='rules'),
]
