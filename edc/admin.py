from django.contrib import admin
from .models import Hackathon,Hack_Topics,Sponsors,Registration,Submission,Result,BioWorkshop,RegisterWS,Team_Members
# Register your models here.

class TopicTab(admin.TabularInline):
    model = Hackathon.topics.through
    extra = 1

class SponsorTab(admin.TabularInline):
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
    inlines = [TopicTab,SponsorTab,ResultAdmin]

class MemberAdmin(admin.TabularInline):
    model = Registration.members.through
    extra = 1

class HackSubmission(admin.StackedInline):
    model = Submission
    extra = 0

class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Team Details', {'fields':['reg_id','hack_model','team_name','leader','members']}),
        ('Registration Status', {'fields':['registered','payment','pay_id','hack_submitted_at']}),
    ]
    readonly_fields = ('reg_id','pay_id','payment','hack_submitted_at')
    inlines = [MemberAdmin,HackSubmission]

class WorkshopRegister(admin.StackedInline):
    readonly_fields = ('reg_id','pay_id','payment')
    model = RegisterWS
    extra = 0

class WorkshopAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Details', {'fields':['id','title','desc','ws_time','price','img','view_image']}),
        ('Display Details', {'fields':['display','reg_link','link','preference']}),
    ]
    readonly_fields = ('id',)
    inlines = [WorkshopRegister]

class SponsorAdmin(admin.ModelAdmin):
    fields = ['name','logo','view_image']
    readonly_fields = ('view_image',)

admin.site.register(Hackathon,HackAdmin)
admin.site.register(Registration,TeamAdmin)
admin.site.register(BioWorkshop,WorkshopAdmin)
admin.site.register(Hack_Topics)
admin.site.register(Sponsors,SponsorAdmin)
admin.site.register(Team_Members)