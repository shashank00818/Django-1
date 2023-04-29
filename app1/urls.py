from django.urls import path
from app1.views import hello_world
# from . import views

urlpatterns = [
    path('hello', hello_world),
]