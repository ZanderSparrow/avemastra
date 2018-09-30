from django.shortcuts import render, get_object_or_404
from .models import ModelItem

def home(request):
    return render(request, 'game/home.html', {})

def model_item_list(request):
    items = ModelItem.objects.all()
    return render(request, 'game/item_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(ModelItem, pk=pk)
    return render(request, 'game/item_detail.html', {'item': item})

def rules(request):
    return render(request, 'game/rules.html', {})
