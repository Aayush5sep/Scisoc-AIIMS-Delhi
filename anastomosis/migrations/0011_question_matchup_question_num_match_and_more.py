# Generated by Django 4.1.4 on 2022-12-27 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anastomosis', '0010_alter_registration_quiz_submitted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='matchup',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='num_match',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='is_correct',
            field=models.BooleanField(default=False, verbose_name='Mark Correct'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='question_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anastomosis.question', verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='quiz_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anastomosis.quiz', verbose_name='Quiz Name'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='sol_by_participant',
            field=models.TextField(blank=True, null=True, verbose_name='Solution By Participant'),
        ),
    ]