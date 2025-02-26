from django.shortcuts import render
from .models import Customer

def customer_list(request):
   customers = Customer.objects.only('id', 'full_name', 'phone_number', 'pending_amount')
    return render(request, 'customer_list.html', {'customers': customers})
