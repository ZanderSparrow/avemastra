from django.contrib import admin
from .models import Character, ModelItem, RealItem, Monster

admin.site.register(Character)
admin.site.register(ModelItem)

admin.site.register(RealItem)
admin.site.register(Monster)
