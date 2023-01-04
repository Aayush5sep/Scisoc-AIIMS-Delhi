from django.db import models
import uuid
from django.contrib.auth.models import User
from payment.models import Payment

# Create your models here.

class Hack_Topics(models.Model):
    title = models.CharField("Hackathon Topic",max_length=100)
    desc = models.TextField("Description Of Hackathon Topic")

    def __str__(self):
        return self.title[:25]


class Sponsors(models.Model):
    name = models.CharField("Sponsor Name",max_length=50)
    logo = models.ImageField("Sponsor Logo",upload_to='edc/sponsors/')

    def __str__(self):
        return self.name


class Hackathon(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    name = models.CharField("Hackathon Title",max_length=50)
    desc = models.TextField("About Hackathon")
    poster = models.ImageField("Hackathon Poster",upload_to='edc/hackathon/posters/',null=True,blank=True)
    topics = models.ManyToManyField(Hack_Topics)
    sponsors = models.ManyToManyField(Sponsors)
    reg_price = models.IntegerField("Registration Cost(if any)",default=0)
    team_cnt = models.IntegerField("Max Members In 1 Team",default=1)
    display = models.BooleanField("Display On Web?", default=False)
    reg_open = models.BooleanField("Registration Opened?",default=False)
    show_topics = models.BooleanField("View Topics To All?",default=False)
    hack_live = models.BooleanField("Hackathon Started?",default=False)
    on_web = models.BooleanField("Conduct on SciSoc Website?",default=True)
    hack_or_reg_link = models.URLField("Link for Registration/Hackathon",null=True,blank=True)

    def __str__(self):
        return self.name


class Team_Members(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Registration(models.Model):
    reg_id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    registered = models.BooleanField("Registration Valid?",default=False)
    pay_id = models.CharField("Payment Details",max_length=200,null=True,blank=True)
    payment = models.ForeignKey(Payment,on_delete=models.DO_NOTHING,null=True,blank=True,related_name="Hackathon_Payment")
    hack_model = models.ForeignKey(Hackathon,on_delete=models.CASCADE)
    team_name = models.CharField("Team Name",max_length=25)
    leader = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Hackathon_Team_Leader")
    members = models.ManyToManyField(Team_Members)
    hack_submitted_at = models.DateTimeField("Time Of Hackathon Submission",default=None,null=True,blank=True)

    def __str__(self):
        return self.team_name


class Submission(models.Model):
    hack = models.ForeignKey(Hackathon,on_delete=models.CASCADE)
    team = models.ForeignKey(Registration,on_delete=models.CASCADE)
    content = models.FileField(upload_to='edc/hackathon/',null=True,blank=True)

    def __str__(self):
        return self.team.team_name


class Result(models.Model):
    hack = models.ForeignKey(Hackathon,on_delete=models.CASCADE)
    position = models.CharField("Rank In Words OR Numeric",max_length=10)
    submission = models.ForeignKey(Submission,on_delete=models.CASCADE)

    def __str__(self):
        return self.hack.name[:15] + " " + self.position + " " + self.submission.team.team_name[:15]


class BioWorkshop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField("Bio-Workshop Title",max_length=50)
    desc = models.TextField("More About The Workshop")
    img = models.ImageField("Cover Photo",upload_to='insight/workshop/')
    ws_time = models.DateTimeField("Workshop Date And Time")
    display = models.BooleanField("Display On Web?", default=False)
    link = models.URLField("Link If Conducted Online(Add on start)",null=True,blank=True)
    preference = models.IntegerField("Preference",default=1)
    price = models.IntegerField("Workshop Price",default=0)

    def __str__(self):
        return self.title


class RegisterWS(models.Model):
    reg_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    workshops = models.ForeignKey(BioWorkshop, on_delete=models.CASCADE)
    pay_id = models.CharField(max_length=200,null=True,blank=True)
    payment = models.ForeignKey(Payment,on_delete=models.DO_NOTHING,null=True,blank=True,related_name="BioWorkshop_Payment")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name