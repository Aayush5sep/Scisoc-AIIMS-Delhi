# Generated by Django 4.1.4 on 2022-12-26 08:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('journalclub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TWCAOS',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Curate Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(default='', upload_to='curates/', verbose_name='Cover Photo')),
                ('live_date', models.DateTimeField(verbose_name='Start Date And Time')),
                ('display', models.BooleanField(default=False, verbose_name='Display on website')),
            ],
        ),
        migrations.CreateModel(
            name='TWCAOS_Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=20, verbose_name='Platform Name')),
                ('link', models.URLField(verbose_name='Platform Link')),
                ('online', models.BooleanField(default=False, verbose_name='Display link on website?')),
                ('twcaos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journalclub.twcaos')),
            ],
        ),
        migrations.CreateModel(
            name='TWCAOS_Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Guest Name')),
                ('desc', models.CharField(max_length=100, verbose_name='About Guest')),
                ('preference', models.IntegerField(default=1, verbose_name='Higher Rating for upper view')),
                ('twcaos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journalclub.twcaos')),
            ],
        ),
    ]