from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class quiz(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    reg_open = models.BooleanField(default=False)
    on_web = models.BooleanField(default=True)
    quiz_or_reg_link = models.URLField(null=True,blank=True)
    quiz_live = models.BooleanField(default=False)
    reg_price = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Quizzes'

class registration(models.Model):
    reg_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quiz_model = models.ForeignKey(quiz,on_delete=models.CASCADE)
    registered = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=200,null=True,blank=True)

    def get_marks(self):
        solns = solution.objects.filter(reg=self,quiz_id=self.quiz_model)
        total = 0
        for soln in solns:
            if soln.is_correct:
                total += soln.question_detail.marks
        return total

    def __str__(self):
        return self.user


class question(models.Model):
    qid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    quiz_model = models.ForeignKey(quiz,on_delete=models.CASCADE)
    question_detail = models.CharField(max_length=250)
    image = models.ImageField(upload_to='anastomosis/',null=True,blank=True)
    answer = models.TextField(null=True,blank=True)
    marks = models.IntegerField(default=1)
    choices = models.BooleanField(default=False)
    short_answer = models.BooleanField(default=False)
    numerical = models.BooleanField(default=False)

    def __str__(self):
        return self.question_detail

class choice(models.Model):
    question_id = models.ForeignKey(question,on_delete=models.CASCADE)
    option = models.CharField(max_length=50)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option

class solution(models.Model):
    reg = models.ForeignKey(registration,on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(quiz,on_delete=models.CASCADE)
    question_detail = models.ForeignKey(question,on_delete=models.CASCADE)
    sol_by_participant = models.TextField(null=True,blank=True)
    is_correct = models.BooleanField(default=False)