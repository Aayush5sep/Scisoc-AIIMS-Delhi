from django.shortcuts import render,redirect
from .models import quiz,registration,question,solution,choice
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def frontpage(request):
    quizzes = quiz.objects.filter(Q(reg_open = True) | Q(quiz_live = True))
    return render(request,'anastomosis/frontpage.html',{'quizzes':quizzes})

@login_required(login_url='user/login')
def register_quiz(request,qid):
    qz = quiz.objects.get(id=qid)
    regis =registration.objects.filter(quiz_model=qz,user=request.user,registered=True)

    if len(regis)>0:
        return HttpResponse("You have already registered for this quiz....")

    if not qz:
        return HttpResponse("No such quiz exists")

    if qz.reg_price==0:
        registration(user = request.user, quiz_model = qz, registered = True).save()
        messages.success(request,"Registered Successfully")
        return redirect('anastomosis/')
    else:
        # Payment & then save in registration
        # registration(user = request.user, quiz_model = qz, registered = True).save()
        pass

@login_required(login_url='user/login')
def live_quiz(request,qid):
    qz = quiz.objects.get(id=qid)
    regis =registration.objects.get(quiz_model=qz,user=request.user,registered=True)

    if not qz:
        return HttpResponse("No such quiz exists")

    if not regis:
        return HttpResponse(" You have not registered for this quiz :( ")
    
    questions = question.objects.filter(quiz_model=qz)
    question_list = []
    for qn in questions:
        choices = choice.objects.filter(question_id=qn)
        question_list.append({"question":qn,"choices":choices})
    return render(request,'anastomosis/quiz.html',{'reg_id':regis.reg_id,'quiz_id':qz.id,'question_list':question_list})

@login_required(login_url='user/login')
def submit_quiz(request,qid):
    pass