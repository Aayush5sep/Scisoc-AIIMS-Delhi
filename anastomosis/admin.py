from django.contrib import admin
from .models import quiz,registration,question,choice,solution
# Register your models here.

class RegistrationAdmin(admin.StackedInline):
    readonly_fields = ('reg_id','pay_id','payment')
    model = registration
    extra = 0

class QuizAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    inlines = [RegistrationAdmin]

class ChoiceAdmin(admin.StackedInline):
    model = choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('qid','qn_image')
    inlines = [ChoiceAdmin]

class SolutionAdmin(admin.StackedInline):
    model = solution
    readonly_fields = ['quiz_id','question_detail','sol_by_participant','qn_image']
    extra = 0

class RegisteredAdmin(admin.ModelAdmin):
    readonly_fields = ('reg_id','pay_id','payment')
    inlines = [SolutionAdmin]

admin.site.register(quiz,QuizAdmin)
admin.site.register(question,QuestionAdmin)
admin.site.register(registration,RegisteredAdmin)