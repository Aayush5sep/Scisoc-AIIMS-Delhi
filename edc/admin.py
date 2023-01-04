from django.contrib import admin
from .models import Hackathon,Hack_Topics,Sponsors,Registration,Submission,Result,BioWorkshop,RegisterWS
# Register your models here.

admin.site.register(Hackathon)
admin.site.register(Hack_Topics)
admin.site.register(Sponsors)
admin.site.register(Registration)
admin.site.register(Submission)
admin.site.register(Result)
admin.site.register(BioWorkshop)
admin.site.register(RegisterWS)