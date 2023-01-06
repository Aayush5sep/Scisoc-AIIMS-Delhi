from django.db import models
from django.contrib.auth.models import User
import uuid
from payment.models import Payment

# Create your models here.

class Insight(models.Model):
    title = models.CharField("Insight Title",max_length=50)
    desc = models.TextField("About Insight")
    fest_img = models.ImageField("Fest Image",upload_to='insight/images/')
    brochure_img = models.ImageField("Brochure Image", upload_to='insight/images/')
    start = models.DateField("Start Date Of Insight")
    live = models.BooleanField("Display On Web?",default=False)

    def __str__(self):
        return self.title


class Workshop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    insight = models.ForeignKey(Insight,on_delete=models.CASCADE)
    title = models.CharField("Workshop Title",max_length=50)
    desc = models.TextField("More About The Workshop")
    img = models.ImageField("Cover Photo",upload_to='insight/workshop/')
    ws_time = models.DateTimeField("Workshop Date And Time")
    reg_link = models.URLField("External Registration Link",null=True,blank=True)
    link = models.URLField("Link If Conducted Online",null=True,blank=True)
    preference = models.IntegerField("Preference",default=1)
    price = models.IntegerField("Workshop Price",default=0)

    def __str__(self):
        return self.title


class RegisterWorkshop(models.Model):
    reg_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    workshops = models.ManyToManyField(Workshop)
    free_collec = models.BooleanField("Free Collection?",default= False)
    registered = models.BooleanField("Registration Valid?", default=False)
    pay_id = models.CharField(max_length=200,null=True,blank=True)
    payment = models.ForeignKey(Payment,on_delete=models.DO_NOTHING,null=True,blank=True,related_name="Workshop_Payment")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Events(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    insight = models.ForeignKey(Insight,on_delete=models.CASCADE)
    title = models.CharField("Event Title",max_length=50)
    desc = models.TextField("More About The Event")
    img = models.ImageField("Cover Photo",upload_to='insight/event/')
    event_time = models.DateTimeField("Event Date And Time")
    reg_link = models.URLField("External Registration Link",null=True,blank=True)
    link = models.URLField("Link (If Conducted Online)",null=True,blank=True)
    preference = models.IntegerField("Preference",default=1)
    price = models.IntegerField("Entry Price (if any)",default=0)
    result = models.BooleanField("Display Result (if any)",default=False)

    def __str__(self):
        return self.title

class RegisterEvent(models.Model):
    reg_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    events = models.ManyToManyField(Events)
    free_collec = models.BooleanField("Free Collection?",default= False)
    registered = models.BooleanField("Registration Valid?", default=False)
    pay_id = models.CharField(max_length=200,null=True,blank=True)
    payment = models.ForeignKey(Payment,on_delete=models.DO_NOTHING,null=True,blank=True,related_name="Event_Payment")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class InsightResult(models.Model):
    event = models.ForeignKey(Events,on_delete=models.CASCADE)
    position = models.CharField("Rank In Words OR Numeric",max_length=10)
    reg = models.ForeignKey(RegisterEvent,on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title[:15] + " " + self.position + " " + self.reg.user.first_name[:15]