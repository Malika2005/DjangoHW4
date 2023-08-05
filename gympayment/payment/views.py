from django.shortcuts import render
from .models import Customer

def gym_payment_status(request):
    customers = Customer.objects.all
    return render(request, 'payment_status.html', {'customers': customers})
