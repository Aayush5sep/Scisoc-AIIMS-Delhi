from django.contrib import admin
from django.contrib.auth.models import User
from .models import PositionDetails,UserDetails

class UserDetailAdmin(admin.StackedInline):
    model = UserDetails

class PositionAdmin(admin.StackedInline):
    model = PositionDetails

class MyUserAdmin(admin.ModelAdmin):
    readonly_fields = ('password')
    inlines = [UserDetailAdmin,PositionAdmin]

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(PositionDetails)
