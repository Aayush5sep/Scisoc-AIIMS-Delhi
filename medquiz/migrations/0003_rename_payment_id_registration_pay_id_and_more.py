# Generated by Django 4.1.5 on 2023-01-03 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
        ('medquiz', '0002_quiz_poster_alter_question_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='payment_id',
            new_name='pay_id',
        ),
        migrations.AddField(
            model_name='registration',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Medquiz_Payment', to='payment.payment'),
        ),
    ]
