from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request,'about.html')

def home(request):
    return render(request, 'home.html')

def cv(request):
    return render(request, 'cv.html')

def contacts(request):
    return render(request, 'contacts.html')

def my_job(request):
    return render(request, 'my_job.html')
