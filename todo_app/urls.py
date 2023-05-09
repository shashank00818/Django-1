from django.urls import path
from todo_app.views import index_view

urlpatterns = [
    path('index', index_view)
    # path('hii', hii_world),
    # path('person-info/<int:person_id>', person_info)
]