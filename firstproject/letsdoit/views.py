from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from .models import Myinfo

def home(request):
    myinfos=Myinfo.objects.all()
    return render(request,'home.html',{'myinfos':myinfos})



def myinfo_detail(request,id):
    try:
        myinfo=Myinfo.objects.get(id=id)
    except Myinfo.DoesNotExist:
        raise Http404('page not foiund')
    return render(request,'myinfo_details.html',{'myinfo':myinfo })     



