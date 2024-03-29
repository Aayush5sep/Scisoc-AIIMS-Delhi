from django.db import models
from django.contrib.auth.models import User
import uuid
from payment.models import Payment
from django.utils.html import mark_safe
from django.db.models.signals import post_delete
import os
from django.dispatch import receiver

# Create your models here.

class Insight(models.Model):
    title = models.CharField("Insight Title",max_length=50)
    desc = models.TextField("About Insight")
    video = models.FileField("Fest Video",upload_to='insight/videos',null=True,blank=True)
    img = models.ImageField("Fest Image",upload_to='insight/images',null=True,blank=True)
    start = models.DateField("Start Date Of Insight")
    live = models.BooleanField("Display On Web?",default=False)

    def __str__(self):
        return self.title

    def view_image(self):
        return mark_safe('<img src="/media/%s" width="250" max-height="250" />' % (self.fest_img))
    view_image.short_description = 'Image'

    class Meta:
        ordering = ["-start"]
        verbose_name_plural = "Insight"

@receiver(post_delete, sender=Insight)
def insight_delete(sender,instance, **kwargs):
    if instance.video:
        if os.path.isfile(instance.video.path):
            os.remove(instance.video.path)
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)

class Sponsor(models.Model):
    insight = models.ForeignKey(Insight,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    logo = models.ImageField(upload_to='insight/images')

    def __str__(self):
        return self.name

@receiver(post_delete, sender=Sponsor)
def insight_delete(sender,instance, **kwargs):
    if instance.logo:
        if os.path.isfile(instance.logo.path):
            os.remove(instance.logo.path)


class Speaker(models.Model):
    insight = models.ForeignKey(Insight,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='insight/images')
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.name

@receiver(post_delete, sender=Speaker)
def insight_delete(sender,instance, **kwargs):
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)


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

    def view_image(self):
        return mark_safe('<img src="/media/%s" width="250" max-height="250" />' % (self.img))
    view_image.short_description = 'Image'

    class Meta:
        ordering = ["preference"]
        verbose_name_plural = "Workshops"

@receiver(post_delete, sender=Workshop)
def insight_delete(sender,instance, **kwargs):
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)


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

    class Meta:
        verbose_name_plural = "Workshop Registrations"


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

    def view_image(self):
        return mark_safe('<img src="/media/%s" width="250" max-height="250" />' % (self.img))
    view_image.short_description = 'Image'

    class Meta:
        ordering = ["preference"]
        verbose_name_plural = "Events"

@receiver(post_delete, sender=Events)
def insight_delete(sender,instance, **kwargs):
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)


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

    class Meta:
        verbose_name_plural = "Event Registrations"


class InsightResult(models.Model):
    event = models.ForeignKey(Events,on_delete=models.CASCADE)
    position = models.CharField("Rank In Words OR Numeric",max_length=10)
    reg = models.ForeignKey(RegisterEvent,on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title[:15] + " " + self.position + " " + self.reg.user.first_name[:15]

    class Meta:
        verbose_name_plural = "Event's Result"