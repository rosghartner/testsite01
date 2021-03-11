from main.forms import TaskForm
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from.models import Task
from.forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id') 
    # tasks = Task.objects.all() 
    return render(request,'main/index.html',{'title': 'Главная страница сайта', 'tasks':tasks})

def huindex(request):
    return render(request,'main/about.html')
   # return HttpResponse("<h1>lol kek cheburek</h1> <hr> ") #HttpResponse это строка через нее неудобно выводить много текста

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма была неверной'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request,'main/create.html', context)