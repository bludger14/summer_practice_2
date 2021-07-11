from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

from django.core.paginator import Paginator
from .models import Song


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Упс, что-то пошло не так'


    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)


def music(request):
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "main/music.html", context)