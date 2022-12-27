from django.contrib import admin
from .models import quiz,registration,question,choice,solution
# Register your models here.

class RegistrationAdmin(admin.StackedInline):
    model = registration

class QuizAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    inlines = [RegistrationAdmin]

class ChoiceAdmin(admin.StackedInline):
    model = choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('qid',)
    inlines = [ChoiceAdmin]

class SolutionAdmin(admin.StackedInline):
    model = solution
    readonly_fields = ['quiz_id','question_detail','sol_by_participant']
    extra = 0

class RegisteredAdmin(admin.ModelAdmin):
    readonly_fields = ('reg_id',)
    inlines = [SolutionAdmin]

admin.site.register(quiz,QuizAdmin)
admin.site.register(question,QuestionAdmin)
admin.site.register(registration,RegisteredAdmin)