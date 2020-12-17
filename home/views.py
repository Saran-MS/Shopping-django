from django.shortcuts import render,redirect
from .models import shop,Cart
import datetime
from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):
    return render(request, 'index.html')

def shops(request):
    val = shop.objects.all()
    return render(request, 'shop.html', {'shop': val})

def buy(request, id):
    val = shop.objects.get(id=id)
    return render(request,'description.html',{'obj':val})

def checkout(request,id):
    val = shop.objects.get(id=id)
    return render(request, 'checkout.html',{'obj':val})

def add(request,id):
    val = shop.objects.get(id=id)
    if request.method == 'POST':
        user = request.user.username
        brand = val.brand
        price = val.price
        quantity = request.POST['qua']
        address = request.POST['addr']
        phone = request.POST['mob']
        timestamp = datetime.datetime.now()
        img = val.img
        cart = Cart.objects.create(user=user,brand=brand,price=price, quantity=quantity, address=address,phone=phone,timestamp=timestamp,image=img)
        cart.save()
        return redirect('/cart')

def cart(request):
    val = Cart.objects.all()
    lst=[]
    for i in val:
        if i.user == request.user.username:
            lst.append(i)
        else:
            continue

    return render(request,'cart.html',{'obj':lst})