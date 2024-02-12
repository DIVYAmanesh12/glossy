from django.shortcuts import render,redirect
from .models import *
from seller.models import *
# Create your views here.
def home(request):
    return render(request,'customer/home.html')
def signup(request):
    if request.method=='POST':
        name1=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        cus=Customer(name=name1,email=email,password=password)
        cus.save()
        return redirect('customer:login')
    return render(request,'customer/signup.html')



def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        try:
          cus=Customer.objects.get(email=email,password=password)
          request.session['customer']=cus.id
          return redirect('customer:dashboard')
        except Customer.DoesNotExist:
         return render(request,'customer/login.html',{'msg':'invalid username or password '})
           

   #      if Customer.objects.filter(email=email,password=password).exists():
   #         return redirect('customer:dashboard')
   #      else:
   #       return render(request,'customer/login.html')
    return render(request,'customer/login.html')

def dashboard(request):
   if 'customer' in request.session:
      return render(request,'customer/dashboard.html')
   else:
      return render(request,'customer/home.html')

def eye(request):
   if 'customer' in request.session:
      cat=Category.objects.get(name='EYE')

      pdt=Product.objects.filter(category=cat)
      return render(request,'customer/eye.html',{'products':pdt})
   else:
      return render(request,'customer/home.html')

   

def lipcare(request):
   if 'customer' in request.session:
      cat=Category.objects.get(name='LIPS')
      pdt=Product.objects.filter(category=cat)
      return render(request,'customer/lipcare.html',{'products':pdt})
   else:
      return render(request,'customer/home.html')

   

        
def skincare(request):
   if 'customer' in request.session:
      cat=Category.objects.get(name='SKIN')
      pdt=Product.objects.filter(category=cat)
      return render(request,'customer/skincare.html',{'products':pdt})
   else:
      return render(request,'customer/home.html')
   

def payment(request):
   if 'customer' in request.session:
      return render(request,'customer/payment.html')
   else:
      return render(request,'customer/home.html')

   

def add_to_cart(request,product_id):
   if request.method=='POST':
      product=Product.objects.get(id=product_id)
      cart_item,created=Cart.objects.get_or_create(product=product)
      if not created:
         cart_item.quantity+=1
         cart_item.save()
   return redirect('customer:cart')
def cart(request):
   if 'customer' in request.session:
      cart_items=Cart.objects.all()
      total_price=sum(item.product.price*item.quantity for item in cart_items)
      total_price_per_item=[]
      grand_total=0
      for item in cart_items:
         item_total=item.product.price*item.quantity
         total_price_per_item.append({'item':item,'total':'item_total'})
         grand_total+=item_total
      return render(request,'customer/cart.html',{'cart_items':cart_items,'grand_total':grand_total,'total_price':total_price})
     
   else:
      return render(request,'customer/home.html')

   
   


def remove_from_cart(request,product_id):
     product=Product.objects.get(id=product_id)
     cart_item=Cart.objects.get(product=product)
     cart_item.delete()
     return redirect('customer:cart')
def  about(request):
   return render(request,'customer/about.html')

def  card(request):
   if 'customer' in request.session:
      return render(request,'customer/card.html')
   else:
      return render(request,'customer/home.html')

   

def logout(request):
   if 'customer' in request.session:
      del request.session['customer']
      return redirect('customer:home')
   


def add_to_wishlist(request,product_id):
   if request.method=='POST':
      product=Product.objects.get(id=product_id)
      Wishlist_item,created= Wishlist.objects.get_or_create(product=product)
      if not created:
         Wishlist_item.quantity+=1
         Wishlist_item.save()
   return redirect('customer:wishlist')
def wishlist(request):
   if 'customer' in request.session:
      wishlist_items=Wishlist.objects.all()
      total_price=sum(item.product.price*item.quantity for item in  wishlist_items)
      total_price_per_item=[]
      grand_total=0
      for item in wishlist_items:
         item_total=item.product.price*item.quantity
         total_price_per_item.append({'item':item,'total':'item_total'})
         grand_total+=item_total
      return render(request,'customer/wishlist.html',{'wishlist_items':wishlist_items,'grand_total':grand_total,'total_price':total_price})
     
   else:
      return render(request,'customer/wishlist.html')
   
def remove_from_wishlist(request,product_id):
     product=Product.objects.get(id=product_id)
     wishlist_item=Wishlist.objects.get(product=product)
     wishlist_item.delete()
     return redirect('customer:wishlist')



      










           