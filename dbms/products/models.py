from django.db import models
from django import forms

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
    )
    name = models.CharField(max_length=50)
    prod_code = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=1000, decimal_places=1)
    category = forms.CharField(label='Category:', widget=forms.Select(choices=CATEGORY_CHOICES))
    
    def __str__(self):
        return self.name