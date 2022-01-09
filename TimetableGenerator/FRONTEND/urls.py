from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name="Home"),
    path('generate', views.generate, name="generate"),
    path('', views.signin, name="signin"),
    path('signout', views.signout, name="signout")
]