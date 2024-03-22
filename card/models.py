from django.db import models
from product_store.models import Product
# Create your models here.

class Cart(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=200, default='')
    
    def __str__(self) -> str:
        return self.date_added

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def get_total_price(self):
        return self.quantity * self.product.xozirgi_narx

    def __str__(self) -> str:
        return self.product