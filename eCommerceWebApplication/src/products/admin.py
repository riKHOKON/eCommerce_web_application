from django.contrib import admin

# for using from another applictaion
# from products.models import Product

from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    class Meta:
        model = Product 

admin.site.register(Product, ProductAdmin)