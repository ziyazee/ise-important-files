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
    return HttpResponse("great!!! files got added")
# def getlist(request,id):
#     try:
def details(request,name):
    detail=clasyear.objects.filter(name=name)
    # category=filest.objects.get(categorie=name)
    
    contentValue = {'detail':detail}
    return render(request,'details.html',contentValue)
def subjects(request,year):
    subject=clasyear.objects.filter(year=year)
    return render(request,'subjects.html',{'subject':subject})
def files(request,categorie):
    print(categorie)
    file=filest.objects.filter(categorie=categorie)    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    else:
        form = PostForm( initial = {'categorie'  :categorie})
    return render(request,'files.html',{'file':file,'form':form})


  

