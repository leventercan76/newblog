from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required
# Create your views here.

#context = {"numbers" : [1,2,3,4,5,6] }
def index(request):
    return render(request,"index.html")#,context)

def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)


@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None) # file için request.FILES ekledik
    if form.is_valid():
        
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request,"Makale kaydı başarılı")
        return redirect("index")
    return render(request,"addarticle.html",{"form":form})

@login_required(login_url="user:login")
def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)

    comments = article.comments.all() #related_name = comments
    return render(request,"detail.html",{"article":article, "comments":comments})

@login_required(login_url="user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request,"Makale güncelleme başarılı")
        return redirect("article:dashboard")
    
    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()
    messages.success(request,"Makale {0} silindi".format(id))
    return redirect("article:dashboard")


def articles(request):
    keyword = request.GET.get("aramaKeyword")
    if keyword:
      articles = Article.objects.filter(titles__contains = keyword )  
    else:
        articles = Article.objects.all()
    return render(request,"articles.html",{"articles":articles})

def addComment(request,id):
    article = get_object_or_404(Article,id = id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content") 

        newComment = Comment(article=article,comment_author=comment_author,comment_content=comment_content)
        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id})) #"/articles/article/" + str(id))
    