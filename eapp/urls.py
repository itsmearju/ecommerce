from django.urls import path
from . import views
app_name = 'eapp'

urlpatterns = [

    path('', views.allProducts_page, name = 'allProducts_page'),

    #--------to display products by category-----------#
    path('<slug:cat_slug>/', views.allProducts_page, name = 'products_by_category'),
    path('adminhome', views.adminhome,name='adminhome'),
]