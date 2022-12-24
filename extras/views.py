from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from user.models import Newsletter
from .models import faq,problem
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail,send_mass_mail

# Create your views here.

def contactpage(request):
    fname = ""
    email = ""
    if request.user.is_authenticated:
        fname = request.user.first_name
        email = request.user.email
    return render(request,'contactus.html',{'fname':fname,'email':email})

def contactreq(request):
    name = request.GET['fname']
    email = request.GET['email']
    header = request.GET['header']
    desc = request.GET['desc']
    prob = problem(name=name,email=email,header=header,desc=desc)
    prob.save()
    messages.success("Your problem has been shared with us....")
    return redirect("/")

@staff_member_required
def replypage(request):
    pass

@staff_member_required
def replied(request):
    pass

def faqs(request):
    faq_list = faq.objects.order_by('-rating')
    return render(request,'extras/faqs.html',{'faqs':faq_list})

def announcepage(request):
    pass

def announce(request):
    if request.user.is_superuser:
        subject = request.GET['subject']
        description = request.GET['description']
        subs = Newsletter.objects.filter(sub=True)
        recipients = []
        for sub in subs:
            recipients.append(sub.user.email)
        email_from = settings.EMAIL_HOST_USER
        print(recipients)
        send_mass_mail( ((subject, description, email_from, recipients),), fail_silently=False )

        return HttpResponse("Message sent successfully to all subscribed users.")
    else:
        return HttpResponse("You do not have access to this page")