from django.http import HttpResponse
from django.shortcuts import render
  
def hello_world(request):
    html = "<html><body>You are hitting Hello world view</body></html>"
    return HttpResponse(html)

def hii_world(request):
    my_data = {
        "name" : "Shashank",
        "language" : "Python",
        "dream" : "Django developer"
    }
    return render(request, "hii_world.html", my_data)