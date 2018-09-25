from django.contrib.postgres.fields import ArrayField
from django.db import models

# Models in alphebetical order

# Character
class Character(models.Model):
    player = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
# Item
class Item(models.Model):
    name = models.CharField(max_length=200)
    holder = models.ForeignKey(Character, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name

# Monster
class Monster(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name
