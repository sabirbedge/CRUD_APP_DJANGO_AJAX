from django.shortcuts import render
from django.http import JsonResponse
from .forms import UserForm
from .models import User
#import json
# Create your views here.
def index(request):
    form=UserForm()
    param=User.objects.order_by('-id').values()
    return render(request,'index.html',{'form':form,'param':param })
#index end

#save start 
def save(request):
    if request.method=='POST':
        #saving new data
        if request.POST['type']=='save':
            form=UserForm(request.POST)
            name=request.POST['name'].upper()
            mobile=request.POST['mobile']
            addr=request.POST['addr'].upper()
            obj=User(nm=name,mob=mobile,city=addr)
            obj.save()
            data=User.objects.order_by('-id').values()
            # print(data)
            data_list=list(data)
            #print(data_list)
            return JsonResponse({'status':'save','data_list':data_list})
        
        #updating data
        if request.POST['type']=='editdata':
            form=UserForm(request.POST)
            hideid=request.POST['hideid']
            name=request.POST['name'].upper()
            mobile=request.POST['mobile']
            addr=request.POST['addr'].upper()
            rec=User.objects.all().get(id=hideid)
            rec.nm=name
            rec.mob=mobile
            rec.city=addr
            rec.save()
            data=User.objects.order_by('-id').values()
            data_list=list(data)
            return JsonResponse({'status':'edited','data_list':data_list}) 

        if request.method!='POST':
            return JsonResponse({'status':'notsave'})


#delete start
def delete(request):
    if request.method=='POST':
        id=request.POST['delid']
        obj=User.objects.all().get(id=id)
        print(obj)
        obj.delete()
        data=User.objects.order_by('-id').values()
       # print(data)
        data_list=list(data)
        #print(data_list)
        return JsonResponse({'status':'del','data_list':data_list})
    if request.method!='POST':
        data=User.objects.order_by('-id').values()
       # print(data)
        data_list=list(data)
        #print(data_list)
        return JsonResponse({'status':'del','data_list':data_list})
    

def edit(request): 
        if request.method=='POST':
            if request.POST['type']=='getdata':
                id=request.POST['editid']
                data=User.objects.filter(id=id).values()
                data_list=list(data)
                return JsonResponse({'status':'got','data_list':data_list})
        else:
            return JsonResponse({'status':'notgot'})
        
