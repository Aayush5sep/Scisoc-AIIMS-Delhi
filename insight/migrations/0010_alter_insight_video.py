# Generated by Django 4.1.5 on 2023-02-04 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insight', '0009_alter_insight_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insight',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='insight/videos', verbose_name='Fest Video'),
        ),
    ]