from django.contrib import admin
from ecommerce.models import Product, Cart, Category, User, Order, OrderItem
# Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderItem)



