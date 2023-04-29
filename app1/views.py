from django.http import HttpResponse
  
def hello_world(request):
    html = "<html><body>You are hitting Hello world view</body></html>"
    return HttpResponse(html)