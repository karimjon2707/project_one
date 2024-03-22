from django.db import models

# Create your models here.
class Add_Quality(models.Model):
    color = models.CharField(max_length=200)
    size = models.CharField(max_length=200)

    def __str__(self):
        return self.color