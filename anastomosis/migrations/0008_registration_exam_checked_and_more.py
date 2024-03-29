# Generated by Django 4.1.4 on 2022-12-25 15:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('anastomosis', '0007_alter_question_qid_alter_quiz_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='exam_checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registration',
            name='quiz_submitted_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
