from django.urls import path
from . import views
app_name = 'eapp'

urlpatterns = [

    path('', views.allProducts_page, name = 'allProducts_page'),

    path('adminhome', views.adminhome, name='adminhome'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('logout_user', views.logout_user, name='logout_user'),

    path('add_category', views.add_category, name='add_category'),
    path('save_category', views.save_category, name='save_category'),

]