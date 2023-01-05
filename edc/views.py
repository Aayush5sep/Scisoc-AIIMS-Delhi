from django.shortcuts import render
from django.http import HttpResponse
from .models import Hackathon,Hack_Topics,Sponsors,Team_Members,Registration,Submission,Result,BioWorkshop,RegisterWS
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from payment.views import paypage

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


def hackathon(request,uid):
    hack = Hackathon.objects.get(id=uid,display=True)
    members = hack.team_cnt
    if not hack.show_topics:
        del hack["topics"]
    return render(request,'edc/hackathon.html',{'hack':hack,'members':range(members)})


@login_required(login_url='/user/login/')
def reg_hack(request,uid):
    if request.method=='POST':
        hack = Hackathon.objects.get(id=uid)
        if hack is None:
            return HttpResponse("No Such Hackathon Exists")
        userid = request.POST['leader']
        teamname = request.POST['teamname']
        members = request.POST.getlist('member')
        leaduser = request.user
        team=[]
        for member in members:
            meb = Team_Members(name=member)
            meb.save()
            team.append(meb)
        reg = Registration.objects.get(hack_model=hack,leader=leaduser)
        if reg is not None and reg.registered==True:
            return HttpResponse("You have already registered for this hackathon")
        if reg is None:
            reg = Registration(hack_model=hack,team_name=teamname,leader=leaduser,members=team)
        if hack.reg_price==0:
            reg.registered=True
            reg.save()
        else:
            reg.save()
            paypage(request,hack.reg_price,"hackathon",reg.reg_id)
    else:
        return HttpResponse("Invalid Request")


@login_required(login_url='/user/login/')
def submit_hack(request,uid):
    hack = Hackathon.objects.get(id=uid)
    reg = Registration.objects.get(registered=True,hack_model=hack,leader=request.user)
    if reg is None:
        return HttpResponse("You are not registered for any such hackathon")
    files = request.POST['files']
    reg.hack_submitted_at = timezone.now()
    reg.save()
    Submission(hack=hack,team=reg,content=files).save()
    return HttpResponse("You Submission has been saves successfully")


@login_required(login_url='/user/login/')
def reg_ws(request,uid):
    ws = BioWorkshop.objects.get(id=uid)
    if ws.price==0:
        reg = RegisterWS(user=request.user, workshops=ws, registered=True)
        reg.save()
    else:
        reg = RegisterWS(user=request.user, workshops=ws)
        reg.save()
        paypage(request,ws.price,"bioworkshop",reg.reg_id)