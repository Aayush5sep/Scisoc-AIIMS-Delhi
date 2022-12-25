from django.contrib import admin
from .models import quiz,registration,question,choice,solution
# Register your models here.

class RegistrationAdmin(admin.StackedInline):
    model = registration
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    inlines = [RegistrationAdmin]

class ChoiceAdmin(admin.StackedInline):
    model = choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceAdmin]

class SolutionAdmin(admin.StackedInline):
    model = solution
    extra = 1

class RegisteredAdmin(admin.ModelAdmin):
    inlines = [SolutionAdmin]

admin.site.register(quiz,QuizAdmin)
admin.site.register(question,QuestionAdmin)
admin.site.register(registration,RegisteredAdmin)