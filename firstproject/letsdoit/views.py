from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import clasyear
def home(request):
    yea=clasyear.objects.order_by('year').values('year').distinct()
    return render(request,'home.html',{'yea':yea,})
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# def getlist(request,id):
#     try:
def subjects(request,year):
    subject=clasyear.objects.filter(year=year)
    return render(request,'subjects.html',{'subject':subject})

  

