from django.db import models
from django.db.models.base import Model
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=20,unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="photo/category",blank=True)
    slug = models.SlugField(max_length=20,unique=True)


    def __str__(self):
        return self.name
    
    def manzil_olmoq(self):
        return reverse("category_slug", args=[self.slug])