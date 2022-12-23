from django.db import models

class Latest(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='latest/',default='latest/latest_default.png')
    link = models.URLField(null=True)
    upload_date = models.DateTimeField(auto_now=True)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def delete(self):
        self.image.storage.delete(self.image.name)
        super().delete()

    class Meta:
        verbose_name_plural = "Latest News"

class Gallery(models.Model):
    hidden_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='gallery/',null=False,blank=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    preference = models.IntegerField(default=1)

    def __str__(self):
        return self.hidden_title

    def delete(self):
        self.image.storage.delete(self.image.name)
        super().delete()

    class Meta:
        verbose_name_plural = "Gallery"