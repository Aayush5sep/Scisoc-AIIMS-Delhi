from django.shortcuts import render
from user.models import PositionDetails
from .models import Latest,Gallery
from django.utils import timezone

def homepage(request):
    team = PositionDetails.objects.filter(display_home=True)
    startdate = timezone.now()
    enddate = startdate - timezone.timedelta(days=16)
    latest = Latest.objects.filter(upload_date__range=[enddate, startdate])
    params = {'team':team,'latest':latest}
    return render(request,'index.html',params)

def gallery(request):
    images = Gallery.objects.order_by('-preference')
    return render(request,'gallery.html',{'images':images})