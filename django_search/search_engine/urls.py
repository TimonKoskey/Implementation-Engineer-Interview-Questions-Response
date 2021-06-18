from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search-results', views.search_results, name='results'),
]