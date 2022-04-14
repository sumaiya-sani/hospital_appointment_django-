# Generated by Django 4.0.3 on 2022-04-04 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_doctor_doctor_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='describe',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='specualization',
            field=models.CharField(blank=True, choices=[('Dermatologist', 'Dermatologist'), ('dentist', 'dentist')], default='Dermatologist', max_length=500, null=True),
        ),
    ]