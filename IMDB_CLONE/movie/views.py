from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Movie


class MovieList(ListView):
    model = Movie


class MovieDetail(DetailView):
    model = Movie


