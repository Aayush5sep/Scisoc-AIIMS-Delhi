from django.db import models
from django.contrib.auth.models import User
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

    def delete(self):
        self.image.storage.delete(self.image.name)
        super().delete()

    class Meta:
        verbose_name_plural = "Positions"

class Newsletter(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    sub = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username