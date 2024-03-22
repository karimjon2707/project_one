from django.shortcuts import render
from product_store.models import Product
from .models import *
# Create your views here.

def Home(malumot):
    masulot = Product.objects.all()
    category = Category.objects.all()
    context = {
        "maxsulotlar": masulot,
        "categorya" : category
    }
    return render(malumot, "home.html", context)
