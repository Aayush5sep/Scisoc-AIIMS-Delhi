from django.contrib import admin
from django.contrib.auth.models import User
from .models import PositionDetails,UserDetails,Newsletter

class UserDetailAdmin(admin.StackedInline):
    model = UserDetails

class PositionAdmin(admin.StackedInline):
    model = PositionDetails

class SubsAdmin(admin.StackedInline):
    model = Newsletter

class MyUserAdmin(admin.ModelAdmin):
    readonly_fields = ('password',)
    inlines = [UserDetailAdmin,SubsAdmin,PositionAdmin]

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)