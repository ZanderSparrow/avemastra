from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Common Properties
class Descriptive(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        abstract=True

class Sentient(Descriptive):
    ac = models.IntegerField(default=1, validators=[MaxValueValidator(1000), MinValueValidator(1)])
    max_hp = models.IntegerField(default=1, validators=[MaxValueValidator(10000), MinValueValidator(0)])
    current_hp = models.IntegerField(default=1, validators=[MaxValueValidator(10000), MinValueValidator(0)])

    class Meta:
        abstract=True

# Models in alphebetical order

# Character
class Character(Sentient):
    player = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        db_table = 'character'

# Items
# For conceptual items that could exist
class ModelItem(Descriptive):
    class Meta:
        db_table = 'model_item'

# For actual instances of a conceptual item
class RealItem(ModelItem):
    holder = models.ForeignKey(Character, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'real_item'

# Monster
class Monster(Sentient):
    
    class Meta:
        db_table = 'monster'

