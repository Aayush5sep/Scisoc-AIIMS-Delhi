# Generated by Django 4.1.4 on 2022-12-23 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soc_member', models.BooleanField(default=False)),
                ('position', models.CharField(default='Visitor', max_length=25)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='socheads/')),
                ('preference', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'PositionDetails',
                'ordering': ['-preference'],
            },
        ),
    ]
