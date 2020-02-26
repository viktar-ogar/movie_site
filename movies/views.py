from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie
from .forms import ReviewForm

# OLD VERSION
# class MoviesView(View):

#     '''Список фильмов'''

#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, "movies/movies.html", {'movie_list': movies})

class MoviesView(ListView):

    '''Список фильмов'''

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movies.html"


# OLD VERSION
# class MovieDetailView(View):

#     '''Подробное описание фильма'''

#     def get(self, request, slug):
#         movie = Movie.objects.get(url=slug)
#         return render(request, "movies/moviesingle.html", {'movie': movie})

class MovieDetailView(DetailView):

    '''Подробное описание фильма'''

    model = Movie
    slug_field = "url"
    template_name = "movies/moviesingle.html"


class AddReview(View):

    '''Отзыв'''

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())