from django.shortcuts import render
from .models import Post, Category
from .forms import CommentForm


def blog(request):
    category = Category.objects.all()
    return render(request,'blog.html', {'category':'Главная страница', 'post':'category'})

