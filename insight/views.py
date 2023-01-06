from django.shortcuts import render
from .models import Insight,Workshop,RegisterWorkshop,Events,RegisterEvent,InsightResult
from payment.views import paypage

# Create your views here.

def insight_home(request):
    pass

def insight(request,id):
    fest = Insight.objects.get(id=id,live=True)
    workshops = Workshop.objects.filter(insight=fest)
    events = Events.objects.filter(insight=fest)
    return render(request,'insight/fest.html',{'fest':fest,'workshops':workshops,'events':events})

def reg_ws(request,uid):
    pass

def reg_event(request,uid):
    pass