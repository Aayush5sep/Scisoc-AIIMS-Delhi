from django.contrib import admin
from .models import Hackathon,Hack_Topics,Sponsors,Registration,Submission,Result,BioWorkshop,RegisterWS,Team_Members
# Register your models here.

class TopicAdmin(admin.TabularInline):
    model = Hackathon.topics.through
    extra = 1

class SponsorAdmin(admin.TabularInline):
    model = Hackathon.sponsors.through
    extra = 0

class ResultAdmin(admin.StackedInline):
    model = Result
    extra = 0

class HackAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Details', {'fields':['id','name','desc','reg_price','team_cnt','poster','view_image']}),
        ('Display Details', {'fields':['display','reg_open','show_topics','hack_live']}),
        ('Conducting Platform', {'fields':['on_web','hack_or_reg_link']}),
    ]
    readonly_fields = ('id','view_image')
    inlines = [TopicAdmin,SponsorAdmin,ResultAdmin]

class MemberAdmin(admin.TabularInline):
    model = Registration.members.through
    extra = 1

class HackSubmission(admin.StackedInline):
    model = Submission
    extra = 0

class TeamAdmin(admin.ModelAdmin):
    readonly_fields = ('reg_id','pay_id','payment')
    inlines = [MemberAdmin,HackSubmission]

class WorkshopRegister(admin.StackedInline):
    readonly_fields = ('reg_id','pay_id','payment')
    model = RegisterWS
    extra = 0

class WorkshopAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    inlines = [WorkshopRegister]


admin.site.register(Hackathon,HackAdmin)
admin.site.register(Registration,TeamAdmin)
admin.site.register(BioWorkshop,WorkshopAdmin)
admin.site.register(Hack_Topics)
admin.site.register(Sponsors)
admin.site.register(Team_Members)