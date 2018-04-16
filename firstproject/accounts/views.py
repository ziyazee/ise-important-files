from django.shortcuts import render,redirect
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)  
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('/home/')

    else:
        form=AuthenticationForm() 
    return render(request,'login.html',{'form':form})
def logout_view(request):
    if request.method=='POST':
        logout(request) 
        return redirect('/')   