# Generated by Django 4.1.3 on 2022-12-01 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0003_diagnosis_diag_policy_treatment_treat_policy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacient',
            name='Birth',
            field=models.CharField(max_length=10, verbose_name='Дата рождения'),
        ),
    ]
