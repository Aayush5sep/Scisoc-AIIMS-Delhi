from django.db import models
from django.utils.html import mark_safe
from django.db.models.signals import post_delete
import os
from django.dispatch import receiver

class Latest(models.Model):
    title = models.CharField("Title",max_length=50)
    description = models.TextField("Description",max_length=200)
    image = models.ImageField("Image",upload_to='latest/',default='latest/latest_default.png')
    link = models.URLField("Redirect Link To Website/File",null=True)
    upload_date = models.DateTimeField(auto_now=True)
    important = models.BooleanField("Mark Important?",default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Latest News"
        verbose_name_plural = "Latest News"

@receiver(post_delete, sender=Latest)
def latest_news_delete(sender,instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


class Gallery(models.Model):
    hidden_title = models.CharField("Hidden Title Behind Image",max_length=50)
    image = models.ImageField("Gallery Image",upload_to='gallery/',null=False,blank=False)
    size_images = models.BooleanField("Normal( 183:100 )",default=True)
    size_big = models.BooleanField("Big( 743:410 )",default=False)
    size_tall = models.BooleanField("Tall( 183:205 )",default=False)
    size_wide = models.BooleanField("Wide( 743:200 )",default=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    preference = models.IntegerField("Higher Preference For Upper Display",default=1)

    def __str__(self):
        return self.hidden_title

    def view_image(self):
        return mark_safe('<img src="/media/%s" width="250" max-height="250" />' % (self.image))
    view_image.short_description = 'Image'

    class Meta:
        verbose_name_plural = "Gallery"

@receiver(post_delete, sender=Gallery)
def gallery_post_delete(sender,instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
