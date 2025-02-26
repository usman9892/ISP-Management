from django.shortcuts import render
from .models import Customer

def customer_list(request):
    customers = Customer.objects.only('id', 'name')
    return render(request, 'customer_list.html', {'customers': customers})
