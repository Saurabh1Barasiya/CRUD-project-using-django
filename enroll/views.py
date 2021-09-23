from enroll.models import User
from django.shortcuts import render,HttpResponseRedirect
from .form import Studentdata

# Create your views here.

def addandshow(request):
    if request.method == 'POST':
        fm  = Studentdata(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data["name"]
            em = fm.cleaned_data["email"]
            pw = fm.cleaned_data["password"]
            print(f"your data here {nm} {em} {pw}")
            reg = User(name=nm, email=em, password=pw)
            reg.save()
    else:
        fm = Studentdata()
    fetch_data = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'fetch_data':fetch_data})

def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id) 
        fm  = Studentdata(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id) 
        fm = Studentdata(instance=pi) 
    return render(request,'enroll/update.html',{'form':fm})
      
