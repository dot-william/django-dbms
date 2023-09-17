from django.db import models
from django import forms

# Product Table

class Product(models.Model):
    CATEGORY_CHOICES = (
    ('Electronics','Electronics'),
    ('Food', 'Food'),
    ('Book','Book'),
    )
    prod_id = models.AutoField(primary_key=True)
    date_added = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='...')
    code = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name