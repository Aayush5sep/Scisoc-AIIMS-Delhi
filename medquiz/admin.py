from django.contrib import admin
from .models import Quiz,Registration,Question,Choice,Solution
# Register your models here.

class RegistrationAdmin(admin.StackedInline):
    model = Registration
    extra = 0

class QuizAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Quiz Display', {'fields':['title','desc','reg_price','team_cnt']}),
        ('Optional Display', {'fields':['reg_open','quiz_live']}),
        ('Conducting Platform', {'fields':['on_web','quiz_or_reg_link']}),
    ]
    readonly_fields = ('id',)
    inlines = [RegistrationAdmin]

class ChoiceAdmin(admin.StackedInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Details', {'fields':['quiz_model','question_detail','image','qn_image','answer','marks']}),
        ('Question Type', {'fields':['choices','short_answer','numerical','true_false','matchup','num_match']}),
    ]
    readonly_fields = ('qid','qn_image')
    inlines = [ChoiceAdmin]

class SolutionAdmin(admin.StackedInline):
    model = Solution
    readonly_fields = ['quiz_id','question_detail','sol_by_participant','qn_image']
    extra = 0

class RegisteredAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Registration Details', {'fields':['reg_id','registered','payment_id','quiz_model']}),
        ('Team Details', {'fields':['team_name','leader','members']}),
        ('Checking Details', {'fields':['quiz_submitted_at','exam_checked','get_marks']}),
    ]
    readonly_fields = ('reg_id','payment_id','quiz_submitted_at','get_marks')
    inlines = [SolutionAdmin]

admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Registration,RegisteredAdmin)