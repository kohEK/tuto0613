from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Card(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='card_set')
    card_color = models.CharField(max_length=7)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner},{self.card_color}'
