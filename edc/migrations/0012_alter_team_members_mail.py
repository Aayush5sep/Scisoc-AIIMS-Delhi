# Generated by Django 4.1.5 on 2023-01-08 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc', '0011_team_members_mail_alter_team_members_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_members',
            name='mail',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Team Member Email'),
        ),
    ]
