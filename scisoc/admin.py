from django.contrib import admin
from .models import Latest,Gallery
from user.models import PositionDetails

class LatestAdmin(admin.ModelAdmin):
    list_display = ('title','upload_date','important','link')
    list_display_links = ('title','link')

class GalleryAdmin(admin.ModelAdmin):
    readonly_fields=('view_image',)

admin.site.register(PositionDetails)

admin.site.register(Latest,LatestAdmin)

admin.site.register(Gallery,GalleryAdmin)