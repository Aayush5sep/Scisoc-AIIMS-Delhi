from django.shortcuts import render
from .models import Insight,Workshop,RegisterWorkshop,Events,RegisterEvent,InsightResult
from payment.views import paypage

# Create your views here.

def insight_home(request):
    fests = Insight.objects.filter(live=True).order_by('-start')
    return render(request,'insight/insight.html',{'fests':fests})

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
    prev_reg = RegisterWorkshop.objects.filter(user=request.user,registered=True)
    registered_ws = []
    for prev in prev_reg:
        registered_ws = registered_ws+prev.workshops
    for selec in selected:
        ws = Workshop.objects.get(id=selec)
        if ws.price==0:
            free_ws.append(ws)
        elif ws not in registered_ws:
            amount = amount+ws.price
            workshops.append(ws)
    free_reg = RegisterWorkshop.objects.get(user=request.user,free_collec=True)
    if free_reg is None:
        RegisterWorkshop(user=request.user,workshops=free_ws,registered=True,free_collec=True).save()
    else:
        for freews in free_ws:
            free_reg.workshops.add(freews)
    reg = RegisterWorkshop(user=request.user,workshops=workshops)
    reg.save()
    return paypage(request,amount,"workshop",reg.reg_id)


def reg_event(request):
    selected = request.POST.getlist('event')
    amount = 0
    events = []
    free_ev = []
    prev_reg = RegisterEvent.objects.filter(user=request.user,registered=True)
    registered_ev = []
    for prev in prev_reg:
        registered_ev = registered_ev+prev.events
    for selec in selected:
        evnt = Events.objects.get(id=selec)
        if evnt.price==0:
            free_ev.append(evnt)
        elif evnt not in registered_ev:
            amount = amount+evnt.price
            events.append(evnt)
    free_reg = RegisterEvent.objects.get(user=request.user,free_collec=True)
    if free_reg is None:
        RegisterEvent(user=request.user,events=free_ev,registered=True,free_collec=True).save()
    else:
        for freeev in free_ev:
            free_reg.events.add(freeev)
    reg = RegisterEvent(user=request.user,events=events)
    reg.save()
    return paypage(request,amount,"event",reg.reg_id)