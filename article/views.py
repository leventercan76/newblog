from django.shortcuts import render,HttpResponse

# Create your views here.
context = {"numbers" : [1,2,3,4,5,6] }
def index(request):
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")


# def detail(request,id):
#    return HttpResponse("Detail:"+ str(id))