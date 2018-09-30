from django import forms

from .models import ModelItem

class ModelItemForm(forms.ModelForm):

    class Meta:
        model = ModelItem
        fields = ('name', 'description',)
