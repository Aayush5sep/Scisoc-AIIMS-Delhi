# Generated by Django 4.1.4 on 2023-01-03 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Event Title')),
                ('desc', models.TextField(verbose_name='More About The Event')),
                ('img', models.ImageField(upload_to='insight/event/', verbose_name='Cover Photo')),
                ('event_time', models.DateTimeField(verbose_name='Event Date And Time')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link (If Conducted Online)')),
                ('preference', models.IntegerField(default=1, verbose_name='Preference')),
                ('price', models.IntegerField(default=0, verbose_name='Entry Price (if any)')),
                ('result', models.BooleanField(default=False, verbose_name='Display Result (if any)')),
            ],
        ),
        migrations.CreateModel(
            name='Insight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Insight Title')),
                ('desc', models.TextField(verbose_name='About Insight')),
                ('fest_img', models.ImageField(upload_to='insight/images/', verbose_name='Fest Image')),
                ('brochure_img', models.ImageField(upload_to='insight/images/', verbose_name='Brochure Image')),
                ('start', models.DateField(verbose_name='Start Date Of Insight')),
                ('live', models.BooleanField(default=False, verbose_name='Full Mode Display?')),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Workshop Title')),
                ('desc', models.TextField(verbose_name='More About The Workshop')),
                ('img', models.ImageField(upload_to='insight/workshop/', verbose_name='Cover Photo')),
                ('ws_time', models.DateTimeField(verbose_name='Workshop Date And Time')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link If Conducted Online')),
                ('preference', models.IntegerField(default=1, verbose_name='Preference')),
                ('price', models.IntegerField(default=0, verbose_name='Workshop Price')),
                ('insight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insight.insight')),
            ],
        ),
        migrations.CreateModel(
            name='RegisterWorkshop',
            fields=[
                ('reg_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('payment_id', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workshops', models.ManyToManyField(to='insight.workshop')),
            ],
        ),
        migrations.CreateModel(
            name='RegisterEvent',
            fields=[
                ('reg_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('payment_id', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workshops', models.ManyToManyField(to='insight.events')),
            ],
        ),
        migrations.CreateModel(
            name='InsightResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=10, verbose_name='Rank In Words OR Numeric')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insight.events')),
                ('reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insight.registerevent')),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='insight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insight.insight'),
        ),
    ]
