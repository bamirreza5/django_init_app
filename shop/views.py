from django.shortcuts import render,redirect
from . models import Product
# Create your views here.
def index(request):
    # return redirect('shop')
    return render(request , "index.html" )

def store(request):
    return render(request , "store.html")

def checkout(request):
    return render(request , "checkout.html")

def product(request):
    products = Product.objects.all()
    return render(request  , "product.html" , {'products' : products})
