# Create your views here.
from django.http import HttpResponse
from django.template import loader, Context

def index(request):
    result = HttpResponse("Greetings Osney One")
    return result

def inducks(request):
    t = loader.get_template('inducks.html')
    filler = Context()
    result = HttpResponse(t.render(filler))
    return result

def general(request):
    t = loader.get_template('generic.htplus')

    import time
    now = time.time()
    english = time.strftime("%H:%M", time.gmtime())
    italy = "That was a really <i>expensive</i> ice cream"

    dynamic_bits = Context({'unixtime':now, 'mytime':english, "italy":italy})
    myhtml = t.render(dynamic_bits)
    return HttpResponse(myhtml)

