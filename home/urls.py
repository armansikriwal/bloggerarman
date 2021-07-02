from django.urls import path

from home import views
urlpatterns = [
  path("",views.home,name="home"),
  path("index",views.index,name="index"),
  path("blog/",views.blog,name="blog"),
  path("blogpost/<str:slug>",views.blogpost,name="home"),
  path("contact",views.contact,name="contact"),
  path("search",views.search,name="search")
  
]
    