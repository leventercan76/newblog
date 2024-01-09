from django.contrib import admin
from django.urls import path

from . import views


app_name = "article"

urlpatterns = [
    path("create/",views.index,name="index"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("addarticle/",views.addArticle,name="addarticle"),
    path("article/<int:id>",views.detail,name="detail"),
    path("update/<int:id>",views.update,name="update"),
]