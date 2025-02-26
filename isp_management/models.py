from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=50, unique=True)
   full_name = models.CharField(max_length=100, unique=True)
phone_number = models.CharField(max_length=15, unique=True)
    monthly_bill = models.DecimalField(max_digits=10, decimal_places=2)
    pending_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
