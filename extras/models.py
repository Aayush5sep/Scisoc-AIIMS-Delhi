from django.db import models

# Create your models here.

class faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(max_length=1000)
    order = models.IntegerField(default=100,unique=True)

    def __str__(self):
        return self.question

class problem(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(null=False,blank=False)
    header = models.CharField(max_length=25)
    desc = models.TextField(max_length=400)

    def __str__(self):
        return self.name