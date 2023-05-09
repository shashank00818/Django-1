from django.shortcuts import render

def index_view(request):
    return render(request, "todo_index.html")
# Create your views here.
