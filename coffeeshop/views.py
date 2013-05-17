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

def general(request, pagename=None):
    t = loader.get_template('generic.htplus')

    import time
    now = time.time()
    english = time.strftime("%H:%M", time.gmtime())
    italy = "That was a really <i>expensive</i> ice cream"

    #askedfor = ''
    #if pagename != None:
    #    askedfor = "You asked for " + pagename

    try:
        askedfor = "You asked for " + pagename
    except:
        askedfor = "Go Shopping"


    dynamic_bits = Context({'unixtime':now, 'mytime':english, "italy":italy, "askedfor":askedfor})
    myhtml = t.render(dynamic_bits)
    return HttpResponse(myhtml)

