"""models file"""
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    categories = models.CharField(max_length=200)
    created_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.categories


class SubCategory(models.Model):
    catid = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=200)
    created_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.subcategory