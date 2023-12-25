from django.urls import path
from .views import SchoolAPI, SchoolDetailsAPI

urlpatterns = [
    path('students/', SchoolAPI.as_view()),
    path('students/<int:pk>/', SchoolDetailsAPI.as_view()),
]