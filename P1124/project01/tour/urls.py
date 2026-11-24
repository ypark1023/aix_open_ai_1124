from django.urls import path, include
from . import views

app_name = 'tour'
urlpatterns = [
    path('tour/', views.tour, name='tour'),
]