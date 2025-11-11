from django.http import HttpResponse
from django.template import loader
from .models import Movie
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    peliculas = Movie.objects.all()
    template = loader.get_template('index.html')
    context = {
        'Peliculas': peliculas,        
    }
    return HttpResponse(template.render(context, request))


def Pelicula(request, movie_id):
    Peliculas = Movie.objects.get(id = movie_id)
    template = loader.get_template('display_movie.html')
    context = {
        'Peliculas': Peliculas,
    }
    return HttpResponse(template.render(context, request))

