# Create your views here.
from django.http import HttpResponse
from django.template import loader, Context
from coffeeshop.models import Activity

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

    #Some content
    import time
    now = time.time()
    english = time.strftime("%H:%M", time.gmtime())
    italy = "That was a really <i>expensive</i> ice cream"

    gift = 10000.0
    nn = 17
    pressie = []
    for infavour in range(1,nn+1):
        pressie.append("{0:.2f}".format(gift/infavour))
    
    #askedfor = ''
    #if pagename != None:
    #    askedfor = "You asked for " + pagename
    try:
        askedfor = "You asked for " + pagename
        specific = 1
    except:
        askedfor = "Go Shopping"
        specific = 0

    #Content from the model
    acts = []
    for choice in Activity.objects.all():
        #acts.append(choice.name)
        acts.append(choice)
    selected = []
    if specific:
        for choice in Activity.objects.filter(name=pagename):
            selected.append(choice)

    dynamic_bits = Context({'unixtime':now, 'mytime':english, "italy":italy, "askedfor":askedfor, "tabby":pressie, "acts":acts, "selected":selected})
    myhtml = t.render(dynamic_bits)
    return HttpResponse(myhtml)

