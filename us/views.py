from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from us.models import URL
from django.template import RequestContext
from django.db import models
#Create your views here.
def home(request):
    short_url = None
    if request.method=="POST":
        
        get_url=request.POST.get("url")
        db_url=URL.objects.create(url=get_url)
        db_url.save()
        short_url=db_url.create_short()
    return render_to_response("index.html",
                              {"short_url":short_url},
                               context_instance=RequestContext(request))   
                                 
def link(request,id):
    url=URL.objects.filter(short=id)
    return HTTPResponseRedirect(url.get_url)
