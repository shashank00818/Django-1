from django.urls import path
from app1.views import hello_world, hii_world
# from . import views

urlpatterns = [
    path('hello', hello_world),
    path('hii', hii_world),
]