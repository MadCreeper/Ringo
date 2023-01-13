from django.contrib import admin

# Register your models here.
from .models import Goods, GoodsCategory

admin.site.register(Goods)
admin.site.register(GoodsCategory)