from django.urls import path
from . import views

urlpatterns = [
    path('filter/', views.FilterMoviesView.as_view(), name="filter"),
    path('search/', views.Search.as_view(), name="search"),
    path('categories/', views.CategoriesList.as_view(), name="categories_list"),
    path('category/<str:slug>/', views.CategoryDetail.as_view(), name="category_detail"),
    path('add-rating/', views.AddStarRating.as_view(), name="add_rating"),
    path('json-filter/', views.JsonFilterMoviesView.as_view(), name="json_filter"),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name="movie_detail"),
    path('review/<int:pk>/', views.AddReview.as_view(), name="add_review"),
    path('actor/<str:slug>/', views.ActorView.as_view(), name="actor_detail"),
    path('', views.MoviesView.as_view(), name="movies_list"),
]