from django.contrib import admin
from .models import Order,Shipment,Supplier,Aisle,Item
# Register your models here.


admin.site.register(Order)
admin.site.register(Shipment)
admin.site.register(Supplier)
admin.site.register(Aisle)
#admin.site.register(StorageSpace)
admin.site.register(Item)
