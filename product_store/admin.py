from django.contrib import admin
from .models import *
from quality.models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','slug','descprition', "xozirgi_narx","oldingi_narx" ,'image','aksiya','mavjudmi','category','yaratilgan_vaqt','ozgartirilgan_vaqti']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product,ProductAdmin)
admin.site.register(Add_Quality)
