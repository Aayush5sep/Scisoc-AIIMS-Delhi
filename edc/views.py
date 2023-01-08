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
    workshops = BioWorkshop.objects.filter(display=True).order_by('-preference')
    return render(request,'edc/edcpage.html',{'hacks':hacks,'workshops':workshops})


def hackathon(request,uid):
    hack = Hackathon.objects.get(id=uid,display=True)
    members = hack.team_cnt
    preg = Registration.objects.filter(hack_model=hack,registered=True)
    prev_reg = False
    if len(preg)>0:
        prev_reg = True
    if not hack.show_topics:
        hack = Hackathon.objects.filter(id=uid,display=True).defer('topics')[0]
    results = Result.objects.filter(hack=hack)
    return render(request,'edc/hackathon.html',{'hack':hack,'prev_reg':prev_reg,'members':range(members),'results':results})


@login_required(login_url='/user/login/')
def reg_hack(request,uid):
    if request.method=='POST':
        hack = Hackathon.objects.get(id=uid)
        if hack is None:
            return HttpResponse("No Such Hackathon Exists")
        teamname = request.POST['teamname']
        members = request.POST.getlist('member')
        mebmails = request.POST.getlist('mebmail')
        leaduser = request.user
        team=[]
        for member,mebmail in members,mebmails:
            meb = Team_Members.objects.filter(name__icontains=member,mail=mebmail)
            if len(meb)>0:
                meb = meb[0]
            else:
                meb = Team_Members(name=member,mail=mebmail)
                meb.save()
            team.append(meb)
        reg = None
        try:
            reg = Registration.objects.get(hack_model=hack,leader=leaduser,members=team)
        except:
            print("New Registration")
        if reg is not None and reg.registered==True:
            return HttpResponse("You have already registered for this hackathon")
        if reg is None:
            reg = Registration.objects.create(hack_model=hack,team_name=teamname,leader=leaduser)
            reg.members.set(team)
        if hack.reg_price==0:
            reg.registered=True
            reg.save()
            return HttpResponse("Registered Successfully")
        else:
            reg.save()
            return paypage(request,hack.reg_price,"hackathon",reg.reg_id)
    else:
        return HttpResponse("Invalid Request")


@login_required(login_url='/user/login/')
def submit_hack(request,uid):
    hack = Hackathon.objects.get(id=uid)
    reg = Registration.objects.get(registered=True,hack_model=hack,leader=request.user)
    if reg is None:
        return HttpResponse("You are not registered for any such hackathon")
    sub = Submission.objects.filter(hack=hack,team=reg)
    if len(sub)>0:
        return HttpResponse("You have already submitted...<br><a href='/'>Return To Homepage</a>")
    gitlink = request.POST['gitrepo']
    liveweb = request.POST['hostweb']
    files = request.POST['files']
    reg.hack_submitted_at = timezone.now()
    reg.save()
    Submission(hack=hack,team=reg,content=files,live_host=liveweb,git_link=gitlink).save()
    return HttpResponse("You Submission has been saved successfully <br><a href='/'>Return To Homepage</a>")


@login_required(login_url='/user/login/')
def reg_ws(request,uid):
    ws = BioWorkshop.objects.get(id=uid,display=True)
    reg = RegisterWS.objects.filter(workshops=ws,user=request.user,registered=True)
    if len(reg)>0:
        return HttpResponse("You have already registered for this workshop <br><a href='/'>Return To Homepage</a>")
    if ws.price==0:
        reg = RegisterWS(user=request.user, workshops=ws, registered=True)
        reg.save()
        return HttpResponse("You have been successfully registered for the workshop <br><a href='/'>Return To Homepage</a>")
    reg = RegisterWS(user=request.user, workshops=ws)
    reg.save()
    return paypage(request,ws.price,"bioworkshop",reg.reg_id)