from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('products/', views.products),
    path('customer/', views.customer),
    path('register/',views.regis,name='regis'),
    path('login/',views.loginpage,name='login'),
    path('accounts/login/',views.loginpage,name='login'),
    path('welcome/',views.welcome,name='first'),
    path('logout/', views.logoutUser,name='logout'),
    path('addentry/',views.addentry,name='addentry'),
    path('posts/',views.BlogView.as_view(),name='posts'),
    path('postslist/<int:pk>',views.DetailView.as_view(),name='postslist'),
    path('addpost/',views.AddPostView.as_view(),name='addpost'),
    path('fav/<int:id>/',views.favourite_add,name='favourite_add'),
    path('bookmark/',views.favourite_list,name='book'),
    path('postslist/updatepost/<int:pk>',views.UpdatePostView.as_view(),name='updatepost'),
    path('postslist/<int:pk>/delete',views.DeletePostView.as_view(),name='deletepost'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html") ,name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete")
]
