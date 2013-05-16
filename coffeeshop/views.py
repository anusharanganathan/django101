# Create your views here.
from django.http import HttpResponse

def index(request):
    result = HttpResponse("Greetings Osney One")
    return result
