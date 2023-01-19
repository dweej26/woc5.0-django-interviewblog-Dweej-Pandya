from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('products/', views.products),
    path('customer/', views.customer),
    path('register/',views.regis,name='regis'),
    path('login/',views.loginpage,name='login'),
    path('welcome/',views.welcome,name='first'),
    path('logout/', views.logoutUser,name='logout')
]
