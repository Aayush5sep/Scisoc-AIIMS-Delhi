from django.contrib import admin
from .models import faq,problem
from user.models import Newsletter
# Register your models here.

admin.site.register(faq)
admin.site.register(problem)
admin.site.register(Newsletter)