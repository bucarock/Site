from django.shortcuts import render
from .models import Task

def blog(request):
    task = Task.objects.all()
    return render(request,'blog.html', {'title': 'Главная страница', 'tasks':'title'})




