from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from user.models import PositionDetails
from .models import Latest
from datetime import date, timedelta

def homepage(request):
    team = PositionDetails.objects.filter(display_home=True)
    startdate = date.today()
    enddate = startdate + timedelta(days=11)
    latest = Latest.objects.filter(upload_date__range=[startdate, enddate])
    params = {'team':team,'latest':latest}
    return render(request,'index.html',params)