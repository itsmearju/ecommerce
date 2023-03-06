from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from . models import Category, Products
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout

from eapp import models

# Create your views here.


# def base(request): 
#     return render(request, 'base.html')


#----------------home page ----------#

def allProducts_page(request):
    
    data = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()
    return render(request, 'base.html', {'data':data,'products':products})


def adminhome(request):
    return render(request,'admin_base.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['name']      
        password = request.POST['pswd'] 
       
        user = auth.authenticate(username=username, password=password)   
        if user is not None:   
            if user.is_staff:
                login(request,user)
                return redirect('eapp:adminhome')                #login when user variable has correct values
            else:
                login(request,user)
                auth.login(request,user) 
                #messages.info(request, f'Welcome {username}') 
                return redirect('allProducts_page') 
             
        else:
             #messages.info(request, 'Invalid username or password, Try again')
             return redirect('allProducts_page') 
    else:
        #messages.info(request,'Oops, Please Login ')
        return render(request, 'base.html')  
    
def logout_user(request):
    logout(request)
    return redirect('eapp:allProducts_page')

def add_category(request):  
    return render(request, 'admin_add_cate.html')

def save_category(request):
    if request.method != 'POST':
         messages.error(request, "Invalid Method ")
         return redirect('eapp:add_category')
        
    else:
        cate = request.POST.get('category')

        try: 
           data = models.Category(name=cate)
           data.save()
           messages.success(request, 'New Category added successfully')
           return redirect('eapp:add_category')
        
        except:
             messages.error(request, "Failed to Add Category!")
             return redirect('eapp:add_category')
   