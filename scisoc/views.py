from django.shortcuts import render
from user.models import PositionDetails
from .models import Latest,Gallery
from django.utils import timezone
import random

def homepage(request):
    team = PositionDetails.objects.filter(display_home=True)
    startdate = timezone.now()
    enddate = startdate - timezone.timedelta(days=16)
    latest = Latest.objects.filter(upload_date__range=[enddate, startdate]).order_by('-upload_date')
    params = {'team':team,'latest':latest}
    return render(request,'index.html',params)

def gallery(request):
    imags = Gallery.objects.all()
    images = list(imags)
    random.shuffle(images)
    return render(request,'gallery.html',{'images':images})

def developers(request):
    return render(request,'dev.html')