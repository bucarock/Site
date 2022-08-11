
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog"),
    path("create", views.create, name="create"),
    path("create_blog", views.create_blog, name="create_blog"),
   ]