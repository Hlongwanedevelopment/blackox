from django.contrib import admin
from store.models import (
    Cattle_Stock,
    Sheep_Stock,
    Category,
    Item,
    OrderModel,
    StoreItem
)

# Register your models here.

admin.site.register(Cattle_Stock)
admin.site.register(Sheep_Stock)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(OrderModel)
admin.site.register(StoreItem)