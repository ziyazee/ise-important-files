from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from .models import clasyear
from .models import filest
from .forms import PostForm


def home(request):
    yea=clasyear.objects.order_by('year').values('year').distinct()
    return render(request,'home.html',{'yea':yea,})


def index(request):
    return render(request,'index.html')

def testing(request):
    return render(request,'testing.html')    


def details(request,name):
    detail=clasyear.objects.filter(name=name)
    contentValue = {'detail':detail}
    return render(request,'details.html',contentValue)


def subjects(request,year):
    subject=clasyear.objects.filter(year=year)
    return render(request,'subjects.html',{'subject':subject})


def files(request,categorie):
    print(categorie)
    file=filest.objects.filter(categorie=categorie)    
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm( initial = {'categorie'  :categorie})
    return render(request,'files.html',{'file':file,'form':form})


  

