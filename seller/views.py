from django.shortcuts import render,redirect
from .models import *


# Create your views here.
def home(request):
    return render(request,'seller/home.html')
def s_signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mob=request.POST['mob']
        password=request.POST['password']
        sel=Seller(name=name,email=email,mob=mob,password=password)
        sel.save()
        return redirect('seller:s_login')
    return render(request,'seller/ssignup.html')
def s_login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if Seller.objects.filter(email=email,password=password).exists():
            return redirect('seller:s_dashboard')
        else:
            return render(request,'seller/slogin.html',{'msg':'invalid inputs'})
    return render(request,'seller/slogin.html')
def s_dashboard(request):
    return render(request,'seller/dashboard.html')
def addproduct(request):
    cat=Category.objects.all()

    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        image=request.FILES['image']
        cat=request.POST.get('category')
        category=Category.objects.get(pk=cat)
        pdt=Product(name=name,price=price,image=image,category=category)
        pdt.save()
        return redirect('seller:s_dashboard')
    return render(request,'seller/addpdt.html',{'cat':cat})

def viewpdt(request):
    pdt=Product.objects.all()
    return render(request,'seller/viewpdt.html',{'products':pdt})
def deletepdt(request,pid):
    Product.objects.get(id=pid).delete()
    return redirect('seller:viewpdt')
def updatepdt(request,pid):
    cat=Category.objects.all()
    pdt=Product.objects.get(id=pid)
    if request.method=='POST':
        name1=request.POST['name']
        price1=request.POST['price']
        image1=request.FILES['image']
        cat=request.POST.get('category')
        category1=Category.objects.get(pk=cat)

        pdt.name=name1
        pdt.price=price1
        pdt.image=image1
        pdt.category=category1
        pdt.save()
        return redirect('seller:viewpdt')

    return render (request,'seller/updatepdt.html',{'pdt':pdt,'cat':cat})