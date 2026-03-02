from django.db import models
from django.contrib.auth.models import User
import random
import string

def generate_tracking_number(length=12):
    letters_and_digits = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f"Order #{self.id} - {self.product} by {self.employee.username}"

class Shipment(models.Model):
    name = models.CharField(max_length=100)                # Shipment name
    product = models.CharField(max_length=100)             # Product name
    quantity = models.PositiveIntegerField()               # Quantities
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.status}"

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    company = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



from django.db import models

class Aisle(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    storage_capacity = models.PositiveIntegerField()  # max number of storage spaces in this aisle

    def __str__(self):
        return self.name


class StorageSpace(models.Model):
    aisle = models.ForeignKey(Aisle, on_delete=models.CASCADE, related_name='storage_spaces')
    space_number = models.IntegerField()
    is_filled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.aisle.name} - Space {self.space_number}"


class Item(models.Model):
    aisle = models.ForeignKey(Aisle, on_delete=models.CASCADE, related_name='items')
    storage_space = models.ForeignKey(StorageSpace, on_delete=models.SET_NULL, null=True, blank=True, related_name='items')
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name