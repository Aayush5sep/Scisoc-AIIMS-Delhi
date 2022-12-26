from django.shortcuts import render
from .models import Curate,Curate_Article,TWCAOS,TWCAOS_Guest,TWCAOS_Link,FRYUMS,FRYUMS_Link
# Create your views here.

def curates_list(request):
    curates = Curate.objects.filter(display=True).order_by('-start_date')
    curate_list=[]
    for curate in curates:
        articles = Curate_Article.objects.filter(curate=curate,display=True)
        curate_list.append({"curate":curate,"articles":articles})
    return render(request,'journal/curates.html',{'curates':curate_list})

def twcaos_list(request):
    pass

def fryums_list(request):
    fryums = FRYUMS.objects.filter(display=True).order_by('-live_date')
    fryum_list=[]
    for fryum in fryums:
        links = FRYUMS_Link.objects.filter(fryums=fryum,online=True)
        fryum_list.append({"fryum":fryum,"links":links})
    return render(request,'journal/fryums.html',{'fryums':fryum_list})