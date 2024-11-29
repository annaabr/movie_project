from django.shortcuts import render,redirect
from .models import Films_info
from .forms import Films_info_form
# Create your views here.

def index(request):
    films = Films_info.objects.all()
    return render(request, 'films/index.html', {'films' : films})

def add_info(request):
    error = ''
    if request.method == 'POST':
        form = Films_info_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Данные были заполнены некорректно'
    form = Films_info_form()
    return render(request, 'films/add_info.html', {'form' : form, 'error' : error})