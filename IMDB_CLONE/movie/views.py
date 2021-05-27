from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Movie, Movie_Links


class MovieList(ListView):
    model = Movie
    paginate_by = 1


class MovieDetail(DetailView):
    model = Movie

    def get_object(self):
        object = super(MovieDetail, self).get_object()
        object.views_count += 1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['links'] = Movie_Links.objects.filter(movie=self.get_object())
        return context


class MovieCategory(ListView):
    model = Movie

    def get_queryset(self):
        self.category_id = self.kwargs['pk']
        movies = Movie.objects.filter(category=self.category_id)
        return movies

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context['movie_category'] = self.category_id
        return context
