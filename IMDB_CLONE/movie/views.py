from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Movie


class MovieList(ListView):
    model = Movie
    paginate_by = 1


class MovieDetail(DetailView):
    model = Movie


