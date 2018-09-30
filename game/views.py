from django.shortcuts import render, get_object_or_404, redirect
from .models import ModelItem
from .forms import ModelItemForm

def home(request):
    return render(request, 'game/home.html', {})

def model_item_list(request):
    items = ModelItem.objects.all()
    return render(request, 'game/item_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(ModelItem, pk=pk)
    return render(request, 'game/item_detail.html', {'item': item})

def item_new(request):
    if request.method == "POST":
        form = ModelItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ModelItemForm()
    return render(request, 'game/item_edit.html', {'form': form})


def rules(request):
    return render(request, 'game/rules.html', {})
