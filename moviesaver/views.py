from django.shortcuts import render, redirect
from .models import Movie, Section, Status
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm


def index(request):
    return render(request = request,
    	template_name = 'moviesaver/home.html',
    	context = {"movie":Movie.objects.all().order_by('movie_name')})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("moviesaver:index")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "moviesaver/register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "moviesaver/register.html",
                  context={"form":form})

def sections(request):
    all_movie = Section.objects.all()
    return render(request=request,
                  template_name='moviesaver/sections.html',
                  context={'all_movie': all_movie})

def films(request):
	all_movie = Movie.objects.filter(section="3").order_by('movie_name')
	return render(request = request,
		template_name = 'moviesaver/films.html',
		context={'all_movie':all_movie})

def serials(request):
	section = Movie.objects.filter(section='Сериал').exclude(status='Завершено').order_by('release_date')
	return render(request = request,
		template_name = 'moviesaver/serials.html',
		context={'section':section})


def anime(request):
	return render(request = request, template_name = 'moviesaver/anime.html')

def cartoons(request):
	return render(request = request, template_name = 'moviesaver/cartoons.html')

def logout_request(request):
    logout(request)
    messages.info(request, 'Вы успешно вышли из аккаунта')
    return redirect("moviesaver:index")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Вы успешно вошли {username}')
                return redirect("moviesaver:index")
            else:
                messages.error(request, 'Неправильный логин или пароль')
        else:
            messages.error(request, 'Неправильный логин или пароль')

    form = AuthenticationForm()
    return render(request,
                  "moviesaver/login.html",
                  {"form":form})
