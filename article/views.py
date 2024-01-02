from django.shortcuts import render,HttpResponse
from .forms import ArticleForm

# Create your views here.
context = {"numbers" : [1,2,3,4,5,6] }
def index(request):
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def dashboard(request):
    return render(request,"dashboard.html")


def addArticle(request):
    form = ArticleForm()
    return render(request,"addarticle.html",{"form":form})

# def detail(request,id):
#    return HttpResponse("Detail:"+ str(id))