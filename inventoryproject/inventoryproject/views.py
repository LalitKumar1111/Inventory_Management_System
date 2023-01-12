from django.shortcuts import render
from store.forms import *


def dashboard(request):
    p=Product.objects.all()
    return render(request, 'dashboard.html',{'product':p})