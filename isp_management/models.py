from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(unique=True)(max_length=100)
    phone_number = models.CharField(unique=True)(max_length=15)
    monthly_bill = models.DecimalField(max_digits=10, decimal_places=2)
    pending_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
