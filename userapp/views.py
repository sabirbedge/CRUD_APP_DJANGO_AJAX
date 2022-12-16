from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Demo
from django.db.models import Q
# Create your views here.
def index(request):
    #param=Demo.objects.filter(Q(id=1) | Q(unm='sabir') | Q(unm__startswith='O')).order_by('-id').values()
    if request.method=='POST':
        nm=request.POST['nm']
        mob=request.POST['mob']
        city=request.POST['city']
        d=Demo(nm=nm.lower(),mob=mob.lower(),city=city.lower())
        d.save()
    
    param=Demo.objects.all().order_by('-id').values()
    return render(request,'index.html',{'param':param})

def update(request,id):
    param=Demo.objects.all().filter(id=id).values()
    return render(request,'update.html',{'param':param})

def updateData(request):
    if request.method=='POST':
        uid=request.POST['uid']
        unm=request.POST['unm']
        umob=request.POST['umob']
        ucity=request.POST['ucity']
        d=Demo.objects.all().get(id=uid)
        d.nm=unm.lower()
        d.mob=umob.lower()
        d.city=ucity.lower()
        d.save()
    return redirect('/')

def delete(request,id):
        d=Demo.objects.all().get(id=id)
        d.delete()
        return redirect('/')
