from django.http import HttpResponse
from django.shortcuts import render
  
def hello_world(request):
    html = "<html><body>You are hitting Hello world view</body></html>"
    return HttpResponse(html)

def hii_world(request):
    return render(request, "hii_world.html")