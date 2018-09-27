from django.shortcuts import render
from .models import ModelItem

def home(request):
    return render(request, 'game/home.html', {})

def model_item_list(request):
    items = ModelItem.objects.all()
    return render(request, 'game/item_list.html', {'items': items})
