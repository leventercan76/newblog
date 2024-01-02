from django.shortcuts import render,redirect
from .forms import RegisterForm
from .forms import LoginForm 

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None )
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")       

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.success(request,"Kayıt başarılı")

        return redirect("index")
    else:
        context = {
            "form" : form
        }
    return render(request,"register.html",context)
    """ zahmetli ve karışık daha iyisi var
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")       

            newUser = User(username=username)
            newUser.set_password(password)

            newUser.save()
            login(request,newUser)

            return redirect("index")
        else:
            
            context = {
                "form" : form
            }
            return render(request,"register.html",context)
    else:    
        form = RegisterForm()
        context = {
            "form" : form
        }
        return render(request,"register.html",context) """

def loginUser(request):
    form = LoginForm(request.POST or None )
    context = {
            "form" : form
        }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")       
        user = authenticate(username=username,password=password)
        
        if user is None:
            messages.info(request,"Kullanıcı Adı yada Parola hatalı")
            return render(request,"login.html",context)
        else:
            messages.success(request,"Login başarılı")
            login(request,user=user)
            return redirect("index")
    
        
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    return render(request,"logout.html")