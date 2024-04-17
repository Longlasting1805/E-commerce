from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True, blank=False, null=False)
    username = models.CharField(max_length=100, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    last_name = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
      return self.email

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
      return self.name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    items = models.IntegerField(default=0, blank=False, null=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Available')
    ]

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default= 'P')

    def __str__(self):
     return str(self.items)

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
     return str(self.id)
     

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    description = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
      return str(self.category_id)


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)    

    def __str__(self):
     return str(self.product_id)   
