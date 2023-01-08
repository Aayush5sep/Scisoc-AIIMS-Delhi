from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
# Create your models here.

class UserDetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    phone=models.CharField(max_length=10,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    college = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.user.username

class PositionDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    soc_member = models.BooleanField(default=False)
    position = models.CharField(max_length=25,default="Visitor")
    description = models.TextField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to='socheads/',default='socheads/emptyuser.png')
    display_home = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Positions"

@receiver(post_delete, sender=PositionDetails)
def position_delete(sender,instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


class Newsletter(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    sub = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username