from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    task = Task.objects.all()
    return render(request,'blog.html', {'title': 'Главная страница', 'tasks':'title'})

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        else:
            error = 'Форма была не верной'
    form = TaskForm()
    context = {
        'form':form,
         'error':error
    }
    return render(request,'create.html', context)

def create_blog(request):
    return render(request,'create_blog.html')




