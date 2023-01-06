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

def reg_ws(request):
    selected = request.POST.getlist('workshop')
    amount = 0
    workshops = []
    free_ws = []
    for selec in selected:
        ws = Workshop.objects.get(id=selec)
        if ws.price==0:
            free_ws.append(ws)
        else:
            amount = amount+ws.price
            workshops.append(ws)
    RegisterWorkshop(user=request.user,workshops=free_ws,registered=True).save()
    reg = RegisterWorkshop(user=request.user,workshops=workshops)
    reg.save()
    paypage(request,amount,"workshop",reg.reg_id)


def reg_event(request):
    selected = request.POST.getlist('event')
    amount = 0
    events = []
    free_ev = []
    for selec in selected:
        evnt = Events.objects.get(id=selec)
        if evnt.price==0:
            free_ev.append(evnt)
        else:
            amount = amount+evnt.price
            events.append(evnt)
    RegisterEvent(user=request.user,events=free_ev,registered=True).save()
    reg = RegisterEvent(user=request.user,events=events)
    reg.save()
    paypage(request,amount,"event",reg.reg_id)