from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_request, name='login'),
    path("logout/", views.logoutUser, name='logout'),

    path('category_list/', views.CategoryListView.as_view(), name='category_list'),
    path('category_detail/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('movie_list/', views.MovieListView.as_view(), name='movie_list'),
    path('movie_detail/<int:movie_id>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('search', views.search, name='search'),

]