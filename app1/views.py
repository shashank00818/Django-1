from django.http import HttpResponse
from django.shortcuts import render
from app1.models import Person
  
def hello_world(request):
    html = "<html><body>You are hitting Hello world view</body></html>"
    return HttpResponse(html)

def hii_world(request):
    my_data = {
        "name" : "Shashank",
        "language" : "Python",
        "dream" : "Django developer",
        "person_list" : Person.objects.filter(id__lte=10),
        "oldest_person_list" :  Person.objects.all().order_by('-age')[:10]
    }
    return render(request, "hii_world.html", my_data)

def person_info(request, person_id):
    person_object = Person.objects.get(id=person_id)
    my_data = {
        "name" : person_object.fname,
        "email" : person_object.email
    }
    return render(request, "person_info.html", my_data)