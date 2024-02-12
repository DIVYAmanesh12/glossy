from django.urls import path
from .import views
app_name='customer'
urlpatterns=[
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('eye/',views.eye,name='eye'),
    path('lipcare/',views.lipcare,name='lipcare'),
    path('skincare/',views.skincare,name='skincare'),
    path('payment/',views.payment,name='payment'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name="add_to_cart"),
    path('cart/',views.cart,name='cart'),
    path('remove_from_cart/<int:product_id>',views.remove_from_cart,name='remove_from_cart'),
    path('aboutus/',views.about,name='aboutus'),
    path('card/',views.card,name='card'),
    path('logout/',views.logout,name='logout'),
    path('wishlist/',views.wishlist,name= 'wishlist'),
    path('add_to_wishlist/<int:product_id>/',views.add_to_wishlist,name="add_to_wishlist"),
    path('remove_from_wishlist/<int:product_id>',views.remove_from_wishlist,name='remove_from_wishlist')

]