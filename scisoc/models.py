from django.db import models

class Latest(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='latest/',default='latest/latest_default.png')
    link = models.URLField(null=True)
    upload_date = models.DateTimeField()
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title