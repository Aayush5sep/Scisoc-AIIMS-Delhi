from django.contrib import admin
from .models import Insight,Workshop,RegisterWorkshop,Events,RegisterEvent,InsightResult
# Register your models here.

class WorkShopList(admin.StackedInline):
    readonly_fields = ('id',)
    model = Workshop
    extra = 1

class EventsList(admin.StackedInline):
    readonly_fields = ('id',)
    model = Events
    extra = 1

class InsightAdmin(admin.ModelAdmin):
    readonly_fields = ('view_image',)
    inlines = [WorkShopList,EventsList]

class EventResult(admin.TabularInline):
    model = InsightResult
    extra = 0

class EventAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    inlines = [EventResult]

class WorkshopAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class WorkshopRegister(admin.ModelAdmin):
    readonly_fields = ('reg_id','pay_id','payment')

class EventRegister(admin.ModelAdmin):
    readonly_fields = ('reg_id','pay_id','payment')

admin.site.register(Insight,InsightAdmin)
admin.site.register(Workshop,WorkshopAdmin)
admin.site.register(RegisterWorkshop,WorkshopRegister)
admin.site.register(RegisterEvent,EventRegister)
admin.site.register(Events,EventAdmin)