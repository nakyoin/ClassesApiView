from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey
from rest_framework import serializers

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    size = models.TextField(default='Неизвестно')
    manufactur = models.CharField(max_length=255, default='Безымянный')
    price = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)



    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return str(self.id)

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.name)


class Manufacturer(models.Model):
    firm = models.CharField(max_length=255)
    country = models.CharField(max_length=100)