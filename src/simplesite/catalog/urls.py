from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/<int:pk>', views.about, name='book-detail')
]