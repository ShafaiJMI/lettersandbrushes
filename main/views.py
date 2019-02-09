from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import  Tutorial
from shop.models import Product, Category
from cart.forms import CartAddProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def homepage(request, category_slug=None):
    return render(request =request, template_name="main/home.html", context = {"tutorials": Tutorial.objects.all})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'cart_product_form': cart_product_form
    }
    return render(request, 'main/includes/list.html', context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
           user = form.save()
           username = form.cleaned_data.get('username')
           messages.success(request, f"New Account Created: {username}")
           login(request, user)
           messages.info(request, f"You are now logged in as: {username}")
           return redirect("main:homepage")
        else:
            for msg in form.error_messages:
            	messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = UserCreationForm
    return render(request,
	"main/register.html",
	context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
    	form = AuthenticationForm(request, data=request.POST)
    	if form.is_valid():
    	   username = form.cleaned_data.get('username')
    	   password = form.cleaned_data.get('password')
    	   user = authenticate(username=username, password=password)
    	   if user is not None:
               login(request, user)
               messages.info(request, f"You are now logged in as: {username}")
               return redirect("main:homepage")
           # else:
            #	 messages.error(request, "Invalid username or password")
        #else:
        #    messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request, 
        	      "main/login.html", 
        	      {"form":form})