from django.urls import path
from.import views
app_name='seller'
urlpatterns=[
    path('',views.home,name='home'),
    path('signup/',views.s_signup,name='s_signup'),
    path('s_login/',views.s_login,name='s_login'),
    path('sdashboard',views.s_dashboard,name='s_dashboard'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('viewpdt',views.viewpdt,name='viewpdt'),
    path('deletepdt/<int:pid>',views.deletepdt,name='deletepdt'),
    path('updatepdt/<int:pid>',views.updatepdt,name="updatepdt")
]