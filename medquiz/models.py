from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.html import mark_safe
# Create your models here.

class Quiz(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    title = models.CharField("Quiz Title",max_length=50)
    desc = models.TextField("About Quiz",max_length=500)
    poster = models.ImageField("Quiz Poster",upload_to='medquiz/posters/',null=True,blank=True)
    reg_price = models.IntegerField("Registration Cost(if any)",default=0)
    team_cnt = models.IntegerField("Max Members In 1 Team",default=1)
    reg_open = models.BooleanField("Registration Opened?",default=False)
    quiz_live = models.BooleanField("Quiz Started?",default=False)
    on_web = models.BooleanField("Conduct on SciSoc Website?",default=True)
    quiz_or_reg_link = models.URLField("Link for Registration/Quiz",null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Medillectuals'

class Team_Members(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Registration(models.Model):
    reg_id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    registered = models.BooleanField("Registration Valid?",default=False)
    payment_id = models.CharField("Payment Details",max_length=200,null=True,blank=True)
    quiz_model = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    team_name = models.CharField("Team Name",max_length=25)
    leader = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Team_Leader")
    members = models.ManyToManyField(Team_Members)
    quiz_submitted_at = models.DateTimeField("Time Of Quiz Submission",default=None,null=True,blank=True)
    exam_checked = models.BooleanField("Exam Checked?",default=False)

    def get_marks(self):
        solns = Solution.objects.filter(reg=self,quiz_id=self.quiz_model)
        total = 0
        for soln in solns:
            if soln.is_correct:
                total += soln.question_detail.marks
        return total

    def __str__(self):
        return self.quiz_model.title + " : " + self.leader.username


class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    quiz_model = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    question_detail = models.CharField("Question Detail",max_length=250)
    image = models.ImageField("Question Image",upload_to='medquiz/questions/',null=True,blank=True)
    answer = models.TextField("Solution(hided)",null=True,blank=True)
    marks = models.IntegerField("Marks for correct answer",default=1)
    choices = models.BooleanField("Single/Multiple Correct Choice?",default=False)
    short_answer = models.BooleanField("Short Answer Subjective Question?",default=False)
    numerical = models.BooleanField("Numerical/Integer?",default=False)
    true_false = models.BooleanField("True False Question?",default=False)
    matchup = models.BooleanField("Match The Following Question?",default=False)
    num_match = models.IntegerField("Number of Match options",default=0)

    def __str__(self):
        return self.question_detail

    def delete(self):
        self.image.storage.delete(self.image.name)
        super().delete()
    
    def qn_image(self):
        return mark_safe('<img src="/media/%s" width="250" max-height="250" />' % (self.image))
    qn_image.short_description = 'Image'


class Choice(models.Model):
    question_id = models.ForeignKey(Question,on_delete=models.CASCADE)
    option = models.CharField("Choice Detail",max_length=50)
    is_correct = models.BooleanField("Correct Choice? (hided)",default=False)

    def __str__(self):
        return self.option

class Solution(models.Model):
    reg = models.ForeignKey(Registration,on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(Quiz,on_delete=models.CASCADE,verbose_name="Quiz Name")
    question_detail = models.ForeignKey(Question,on_delete=models.CASCADE,verbose_name="Question")
    sol_by_participant = models.TextField("Solution By Participant",null=True,blank=True)
    is_correct = models.BooleanField("Mark Correct",default=False)

    def qn_image(self):
        return mark_safe('<img src="/media/%s" width="250" max-height="250" />' % (self.question_detail.image))
    qn_image.short_description = 'Image'