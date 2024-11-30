from django.shortcuts import render,HttpResponse
from .forms import ArticleForm
# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def dashboard(request):
    return render(request,"dashboard.html")

def addArticle(request):
    form = ArticleForm()

    return render(request, "addarticle.html",{"form":form})
