# Create your views here.
from django.http import HttpResponse
from django.template import loader, Context
from coffeeshop.models import Activity
from django.core.context_processors import csrf
from django import forms
from django.shortcuts import render_to_response

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

class MyForm(forms.Form):
    name = forms.CharField(max_length=50)
    location = forms.CharField(max_length=50)
    duration = forms.IntegerField()
    description = forms.CharField(widget=forms.TextInput)
    #description = forms.CharField(max_length=200)

def addform(request):
    havesubmission = "Blank form"
    stufftosave = ""
    if request.method == 'POST':
      form = MyForm(request.POST)
      if form.is_valid():
        havesubmission = "We HAVE got data to store"
        stufftosave = "Saving ... " + form.cleaned_data['name']
        stufftosave += ": " + str(form.cleaned_data['location'])
        stufftosave += ": " + str(form.cleaned_data['duration'])
        stufftosave += ": " + str(form.cleaned_data['description'])
        form = MyForm()
      else:
        havesubmission = "Data Invalid - please correct"
    else:
      form = MyForm()
    mycontext = {'formholder': form, 'status': havesubmission, 'saving': stufftosave}
    mycontext.update(csrf(request))
    return render_to_response('formdemo.html',mycontext) 
