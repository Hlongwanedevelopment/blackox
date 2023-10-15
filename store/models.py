from django.db import models
from website.models import Breed, Cattle, Sheep

# Create your models here.

class Cattle_Stock(models.Model):
    cattle = models.ForeignKey(Cattle, on_delete=models.CASCADE, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="cattle_stock/")
    price = models.DecimalField(max_digits=7, decimal_places=2)

class Sheep_Stock(models.Model):
    sheep = models.ForeignKey(Sheep, on_delete=models.CASCADE, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="sheep_stock/")
    price = models.DecimalField(max_digits=7, decimal_places=2)


# For None-Meat Products
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    cattle = models.ForeignKey(Cattle_Stock, on_delete=models.CASCADE, blank=True, null=True)
    sheep = models.ForeignKey(Sheep_Stock, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="menu_images/", blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='i', blank=True, related_name='item')

    def __str__(self):
        return self.name

class StoreItem(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="menu_images/", blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='i', blank=True, related_name='storeitem+')

    def __str__(self):
        return self.name
    
class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    items = models.ManyToManyField('Item', related_name="Items+", blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)

    def __str__(self):
        return f'order: {self.created_on.strftime("%b %d %I: %M %p")}'       
