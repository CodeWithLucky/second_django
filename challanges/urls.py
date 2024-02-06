from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<str:month>/", views.months_challenges, name="month-challenge"),

]