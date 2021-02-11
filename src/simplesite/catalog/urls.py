from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path(r'^book/(?P<pk>\d+)$', views.BookAboutView.as_view(), name = 'book-detail'),
    path('add/', views.BookCreate.as_view(), name = 'book-create'),
    path('create/', views.UserCreate.as_view(), name = 'user-create')
]