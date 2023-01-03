# Generated by Django 4.1.4 on 2023-01-03 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edc', '0002_hackathon_show_topics'),
    ]

    operations = [
        migrations.CreateModel(
            name='BioWorkshop',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Bio-Workshop Title')),
                ('desc', models.TextField(verbose_name='More About The Workshop')),
                ('img', models.ImageField(upload_to='insight/workshop/', verbose_name='Cover Photo')),
                ('ws_time', models.DateTimeField(verbose_name='Workshop Date And Time')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link If Conducted Online')),
                ('preference', models.IntegerField(default=1, verbose_name='Preference')),
                ('price', models.IntegerField(default=0, verbose_name='Workshop Price')),
            ],
        ),
        migrations.CreateModel(
            name='RegisterWS',
            fields=[
                ('reg_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('payment_id', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workshops', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edc.bioworkshop')),
            ],
        ),
    ]
