from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from . models import Category, Products
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login

# Create your views here.


# def base(request): 
#     return render(request, 'base.html')


#----------------home page ----------#

def allProducts_page(request, cat_slug=None):
    cat_page = None
    products = None
    if cat_slug != None:
        cat_page = get_object_or_404(Category, slug=cat_slug)
        products = Products.objects.all().filter(category=cat_page, available=True)
    else:
        products = Products.objects.all().filter(available=True)
    return render(request, 'base.html', {'category':cat_page, 'products':products})


def adminhome(request):
    return render(request,'admin_base.html')

def tlogin(request):
    if request.method == 'POST':
        username = request.POST['username']      
        password = request.POST['password'] 
       
        user = auth.authenticate(username=username, password=password)   
        if user is not None:   
            if user.is_staff:
                login(request,user)
                return redirect('adminhome')                #login when user variable has correct values
            else:
                login(request,user)
                auth.login(request,user) 
                #messages.info(request, f'Welcome {username}') 
                return redirect('customer-home') 

             
        else:
             #messages.info(request, 'Invalid username or password, Try again')
             return redirect('tlogin') 
    else:
        #messages.info(request,'Oops, Please Login ')
        return render(request,'customerlogin.html')  

