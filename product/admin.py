from django.contrib import admin

from .models import Product, Reviews, Category

admin.site.register(Category)
admin.site.register(Reviews)
admin.site.register(Product)

