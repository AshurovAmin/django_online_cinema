from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth import login, logout, authenticate

from .models import Category, Movie


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'category'
    fields = "__all__"


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'
    pk_url_kwarg = 'category_id'


class MovieListView(ListView):
    model = Movie
    template_name = 'movie.html'
    context_object_name = 'movies'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'
    pk_url_kwarg = 'movie_id'


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("movie_list")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


@login_required()
def logoutUser(request):
    logout(request)
    return redirect('/')


def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        movies = Movie.objects.filter(title__icontains=query)
        return render(request, 'search.html', {'movie': movies})
    else:
        return render(request, 'search.html')
