from django.db import models
import uuid
# Create your models here.

class Curate(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4)
    title = models.CharField("Curate Title",max_length=50)
    description = models.TextField("Description")
    image = models.ImageField("Cover Photo",upload_to='curates/',default='')
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date")
    display = models.BooleanField("Display on website",default=False)

    def __str__(self):
        return self.title

class Curate_Article(models.Model):
    curate = models.ForeignKey(Curate,on_delete=models.CASCADE)
    title = models.CharField("Article Title",max_length=50)
    description = models.TextField("Small Description")
    image = models.ImageField("Article Photo",upload_to='curates/',default='')
    author = models.CharField("Article's Author",max_length=50,null=True,blank=True)
    link = models.URLField("Link for the Article")
    display = models.BooleanField("Display In Linked Curate",default=True)

    def __str__(self):
        return self.title

class TWCAOS(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4)
    title = models.CharField("Curate Title",max_length=50)
    description = models.TextField("Description")
    image = models.ImageField("Cover Photo",upload_to='twcaos/',default='')
    live_date = models.DateTimeField("Start Date And Time")
    display = models.BooleanField("Display on website",default=False)

    def __str__(self):
        return self.title

class TWCAOS_Guest(models.Model):
    twcaos = models.ForeignKey(TWCAOS,on_delete=models.CASCADE)
    name = models.CharField("Guest Name",max_length=50)
    desc = models.CharField("About Guest",max_length=100)
    preference = models.IntegerField("Higher Rating for upper view",default=1)

    def __str__(self):
        return self.name

class TWCAOS_Link(models.Model):
    twcaos = models.ForeignKey(TWCAOS,on_delete=models.CASCADE)
    site = models.CharField("Platform Name",max_length=20)
    link = models.URLField("Platform Link")
    online= models.BooleanField("Display link on website?",default=False)

    def __str__(self):
        return self.site

class FRYUMS(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4)
    title = models.CharField("Curate Title",max_length=50)
    description = models.TextField("Description")
    image = models.ImageField("Event Photo",upload_to='fryums/',default='')
    live_date = models.DateTimeField("Start Date And Time")
    display = models.BooleanField("Display on website",default=False)
    author = models.CharField("Guest Name",max_length=50)
    abt_author = models.CharField("About Guest",max_length=100,null=True,blank=True)

    def __str__(self):
        return self.title

class FRYUMS_Link(models.Model):
    fryums = models.ForeignKey(FRYUMS,on_delete=models.CASCADE)
    site = models.CharField("Platform Name",max_length=20)
    link = models.URLField("Platform Link")
    online= models.BooleanField("Display link on website?",default=False)

    def __str__(self):
        return self.site