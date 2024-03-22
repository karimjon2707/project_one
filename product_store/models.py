from django.db import models
from Category.models import Category
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20,unique=True)
    descprition = models.TextField(max_length=500,blank=True)
    xozirgi_narx = models.IntegerField()
    oldingi_narx = models.IntegerField()
    image = models.ImageField(upload_to="photo/product")
    aksiya = models.IntegerField(default=100)
    mavjudmi = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)
    ozgartirilgan_vaqti = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.name
    
    def manzil_olmoq(self):
        return reverse("category_slug", args=[self.slug])




    
    