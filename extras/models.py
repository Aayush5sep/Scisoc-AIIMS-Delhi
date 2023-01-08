from django.db import models

# Create your models here.

class faq(models.Model):
    question = models.CharField("Question",max_length=200)
    answer = models.TextField("Answer(in max 1500 chars)",max_length=1500)
    order = models.IntegerField("Position Number",default=100,unique=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"


class problem(models.Model):
    name = models.CharField("Problem Author",max_length=25)
    email = models.EmailField("Author Email",null=False,blank=False)
    header = models.CharField("Problem Title",max_length=25)
    desc = models.TextField("Problem Description",max_length=400)
    pdate = models.DateField("Query Raised Date & Time",auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "User Query"
        verbose_name_plural = "User Queries"