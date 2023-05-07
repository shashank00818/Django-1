from django.urls import path
from app1.views import hello_world, hii_world, person_info
# from . import views

urlpatterns = [
    path('hello', hello_world),
    path('hii', hii_world),
    path('person-info/<int:person_id>', person_info)
]