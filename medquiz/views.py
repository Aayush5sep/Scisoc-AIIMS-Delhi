from django.shortcuts import render

# Create your views here.

def medsoc(request):
    #  Render Medquiz Society Homepage
    return render(request,'medquiz/mainpage.html')