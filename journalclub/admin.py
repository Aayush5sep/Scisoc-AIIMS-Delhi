from django.contrib import admin
from .models import Curate,Curate_Article,TWCAOS,TWCAOS_Guest,TWCAOS_Link,FRYUMS,FRYUMS_Link
# Register your models here.

class ArticleAdmin(admin.StackedInline):
    model = Curate_Article
    extra = 1

class CurateAdmin(admin.ModelAdmin):
    readonly_fields=('uid',)
    inlines=[ArticleAdmin]

class GuestAdmin(admin.StackedInline):
    model = TWCAOS_Guest
    extra = 1

class PlatformAdmin(admin.StackedInline):
    model = TWCAOS_Link
    extra = 1

class TWCAOSAdmin(admin.ModelAdmin):
    readonly_fields=('uid',)
    inlines=[GuestAdmin,PlatformAdmin]

class LinkAdmin(admin.StackedInline):
    model = FRYUMS_Link
    extra = 1

class FRYUMSAdmin(admin.ModelAdmin):
    readonly_fields=('uid',)
    inlines=[LinkAdmin]

admin.site.register(Curate,CurateAdmin)
admin.site.register(TWCAOS,TWCAOSAdmin)
admin.site.register(FRYUMS,FRYUMSAdmin)
