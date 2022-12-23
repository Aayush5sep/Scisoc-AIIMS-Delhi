from django.contrib import admin
from .models import Latest

class LatestAdmin(admin.ModelAdmin):
    list_display = ('title','upload_date','important','link')
    list_display_links = ('title','link')

admin.site.register(Latest,LatestAdmin)
