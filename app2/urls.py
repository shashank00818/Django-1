from django.urls import path
from app2.views import hi_world

urlpatterns = [
    path("hi", hi_world),
]