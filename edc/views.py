from django.shortcuts import render
from django.http import HttpResponse
from .models import Hackathon,Hack_Topics,Sponsors,Team_Members,Registration,Submission,Result,BioWorkshop,RegisterWS

# Create your views here.

def edc(request):
    live_hacks = Hackathon.objects.filter(display=True,show_topics=True)
    view_hacks = Hackathon.objects.filter(display=True,show_topics=False).defer('topics')
    hacks=[]
    for hack in live_hacks:
        hacks.append(hack)
    for hack in view_hacks:
        hacks.append(hack)
    workshops = BioWorkshop.objects.filter(display=True)
    return render(request,'edc/edcpage.html',{'hacks':hacks,'workshops':workshops})

