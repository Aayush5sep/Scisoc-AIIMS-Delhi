from django.shortcuts import render
from .models import Insight,Workshop,RegisterWorkshop,Events,RegisterEvent,InsightResult,Sponsor,Speaker
from payment.views import paypage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def insight_home(request):
    fests = Insight.objects.filter(live=True).order_by('-start')
    return insight(request,fests[0].id)

def insight(request,id):
    fest = Insight.objects.get(id=id,live=True)
    workshop = Workshop.objects.filter(insight=fest).order_by('preference')
    event = Events.objects.filter(insight=fest).order_by('preference')
    sponsors = Sponsor.objects.filter(insight=fest)
    speakers = Speaker.objects.filter(insight=fest)
    prev_registered = []
    for ws in workshop:
        if RegisterWorkshop.objects.filter(registered=True,workshops__in=[ws]):
            prev_registered.append(True)
        else:
            prev_registered.append(False)
    workshops = []
    if len(workshop)>0:
        workshops = zip(workshop,prev_registered)
    registered_ev = []
    for ev in event:
        if RegisterEvent.objects.filter(registered=True,events__in=[ev]):
            registered_ev.append(True)
        else:
            registered_ev.append(False)
    events = []
    if len(event)>0:
        events = zip(event,registered_ev)
    return render(request,'insight/index.html',{'fest':fest,'workshops':workshops,'events':events,'sponsors':sponsors,'speakers':speakers})

@login_required(login_url='/user/loginpage/')
def reg_ws(request):
    selected = request.POST.getlist('workshop')
    amount = 0
    workshops = []
    free_ws = []
    prev_reg = RegisterWorkshop.objects.filter(user=request.user,registered=True)
    registered_ws = []
    for prev in prev_reg:
        for ws in prev.workshops.all():
            registered_ws.append(ws)
    for selec in selected:
        ws = Workshop.objects.get(id=selec)
        if ws.price==0:
            free_ws.append(ws)
        elif ws not in registered_ws:
            amount = amount+ws.price
            workshops.append(ws)
    free_reg = None
    if RegisterWorkshop.objects.filter(user=request.user,free_collec=True):
        free_reg = RegisterWorkshop.objects.get(user=request.user,free_collec=True)
    if free_reg is None:
        temp_reg = RegisterWorkshop.objects.create(user=request.user,registered=True,free_collec=True)
        temp_reg.workshops.set(free_ws)
    else:
        for freews in free_ws:
            free_reg.workshops.add(freews)
    if amount<=0:
        return HttpResponse("Already Registered")
    reg = RegisterWorkshop.objects.create(user=request.user)
    reg.workshops.set(workshops)
    return paypage(request,amount,"workshop",reg.reg_id)

@login_required(login_url='/user/loginpage/')
def reg_event(request):
    selected = request.POST.getlist('event')
    amount = 0
    events = []
    free_ev = []
    prev_reg = RegisterEvent.objects.filter(user=request.user,registered=True)
    registered_ev = []
    for prev in prev_reg:
        for ev in prev.events.all():
            registered_ev.append(ev)
    for selec in selected:
        evnt = Events.objects.get(id=selec)
        if evnt.price==0:
            free_ev.append(evnt)
        elif evnt not in registered_ev:
            amount = amount+evnt.price
            events.append(evnt)
    free_reg = None
    if RegisterEvent.objects.filter(user=request.user,free_collec=True):
        free_reg = RegisterEvent.objects.get(user=request.user,free_collec=True)
    if free_reg is None:
        temp_reg = RegisterEvent.objects.create(user=request.user,registered=True,free_collec=True)
        temp_reg.events.set(free_ev)
    else:
        for freeev in free_ev:
            free_reg.events.add(freeev)
    if amount<=0:
        return HttpResponse("Already Registered")
    reg = RegisterEvent.objects.create(user=request.user)
    reg.events.set(events)
    return paypage(request,amount,"event",reg.reg_id)