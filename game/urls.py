from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items', views.model_item_list, name='items'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/new', views.item_new, name='item_new'),
    path('rules', views.rules, name='rules'),
]
