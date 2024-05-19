from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Profile

def productspageview(request) :
    data = Product.objects.all()
    context = {"products": data}
    return render(request, "products.html", context)

def profilepageview(request) :
    userdata = Profile.objects.all()
    context = {"profile": userdata}
    return render(request, "profile.html", context)