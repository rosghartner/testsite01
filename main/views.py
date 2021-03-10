from django.shortcuts import render
# from django.http import HttpResponse
from.models import Task


def index(request):
    tasks = Task.objects.order_by('-id') 
    # tasks = Task.objects.all() 
    return render(request,'main/index.html',{'title': 'Главная страница сайта', 'tasks':tasks})

def huindex(request):
    return render(request,'main/about.html')
   # return HttpResponse("<h1>lol kek cheburek</h1> <hr> ") #HttpResponse это строка через нее неудобно выводить много текста
    