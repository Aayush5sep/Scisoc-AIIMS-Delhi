# Generated by Django 4.1.5 on 2023-01-03 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
        ('edc', '0003_bioworkshop_registerws'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registerws',
            old_name='payment_id',
            new_name='pay_id',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='payment_id',
            new_name='pay_id',
        ),
        migrations.AddField(
            model_name='registerws',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='BioWorkshop_Payment', to='payment.payment'),
        ),
        migrations.AddField(
            model_name='registration',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Hackathon_Payment', to='payment.payment'),
        ),
    ]