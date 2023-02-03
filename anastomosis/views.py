from django.shortcuts import render,redirect
from .models import quiz,registration,question,solution,choice
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone
from payment.views import paypage

# Create your views here.

def frontpage(request):
    quizs = quiz.objects.filter(Q(reg_open = True) | Q(quiz_live = True))
    prev_reg = []
    for qz in quizs:
        if registration.objects.filter(user=request.user,quiz_model=qz,registered=True):
            prev_reg.append(True)
        else:
            prev_reg.append(False)
    quizzes = zip(quizs,prev_reg)
    return render(request,'anastomosis/frontpage.html',{'quizzes':quizzes})

@login_required(login_url='/user/loginpage/')
def register_quiz(request,qzid):
    qz = quiz.objects.get(id=qzid)
    regis =registration.objects.filter(quiz_model=qz,user=request.user,registered=True)

    if len(regis)>0:
        return HttpResponse("You have already registered for this quiz....")

    if not qz:
        return HttpResponse("No such quiz exists")

    if qz.reg_price==0:
        registration(user = request.user, quiz_model = qz, registered = True).save()
        messages.success(request,"Registered Successfully")
        return redirect('/anastomosis/')
    else:
        # Payment & then save in registration
        reg = registration(user = request.user, quiz_model = qz)
        reg.save()
        return paypage(request,qz.reg_price,"anastomosis",reg.reg_id)


@login_required(login_url='/user/loginpage/')
def live_quiz(request,qzid):
    qz = quiz.objects.get(id=qzid)
    regis =registration.objects.get(quiz_model=qz,user=request.user,registered=True)

    if not qz:
        return HttpResponse("No such quiz exists")

    if not regis:
        return HttpResponse(" You have not registered for this quiz :( ")

    if regis.quiz_submitted_at is not None:
        return HttpResponse(" You have already submitted your answers ")
    
    questions = question.objects.filter(quiz_model=qz).defer('answer')
    question_list = []
    for qn in questions:
        choices = choice.objects.filter(question_id=qn).defer('is_correct')
        question_list.append({"question":qn,"choices":choices,"iter":range(0,qn.num_match)})
    return render(request,'anastomosis/quiz.html',{'reg_id':regis.reg_id,'quiz_id':qz.id,'quiz_name':qz.title,'question_list':question_list})

@login_required(login_url='/user/loginpage/')
def submit_quiz(request,qzid):
    regid = request.POST['reg_id']
    qz = quiz.objects.get(id=qzid)
    regis =registration.objects.get(quiz_model=qz,user=request.user,registered=True)

    if not qz:
        return HttpResponse("No such quiz exists")

    if not regis:
        return HttpResponse(" You have not registered for this quiz :( ")

    if regis.quiz_submitted_at is not None:
        return HttpResponse(" You have already submitted your answers ")
    
    questions = question.objects.filter(quiz_model=qz)
    for qn in questions:
        qnid = str(qn.qid)
        ans=""
        if qn.choices:
            solns = request.POST.getlist(qnid)
            ans="\n".join(solns)
        elif qn.matchup:
            solns = []
            for iter in range(1,qn.num_match+1):
                solns.append(str(iter)+"->"+request.POST[qnid+"_"+str(iter)])
            ans = "\n".join(solns)
        else:
            ans = request.POST[qnid]
        solution(reg = regis, quiz_id = qz, question_detail = qn, sol_by_participant = ans).save()
    regis.quiz_submitted_at = timezone.now()
    regis.save()
    messages.success(request,"Your answers have been submitted successfully")
    return redirect("/")

# def check_quiz_submissions(request):
#     pass
# def checked_submission(request):
#     pass

@staff_member_required()
def view_marks(request,qzid):
    qz =None
    if quiz.objects.get(id=qzid):
        qz = quiz.objects.get(id=qzid)
    else:
        return HttpResponse("No Such Quiz Found")
    regs = registration.objects.filter(quiz_model=qz,registered=True)
    return render(request,'anastomosis/allmarks.html',{'regs':regs})