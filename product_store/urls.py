from django.urls import path
from .views import *

urlpatterns = [
    path("",Malumot,name="store_panel"),
    path("<slug:category_slug>/", Malumot, name="category_slug"),
    path("view_detail/<int:id>/", Detail, name="detail_name")
]
