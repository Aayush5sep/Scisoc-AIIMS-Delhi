# Generated by Django 4.1.5 on 2023-01-09 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journalclub', '0006_alter_curate_options_alter_curate_article_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fryums',
            options={'verbose_name': 'FRYUMS', 'verbose_name_plural': 'FRYUMS'},
        ),
        migrations.AlterModelOptions(
            name='fryums_link',
            options={'verbose_name': 'FRYUMS Link', 'verbose_name_plural': 'FRYUMS Links'},
        ),
    ]
