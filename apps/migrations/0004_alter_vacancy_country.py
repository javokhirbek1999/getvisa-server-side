# Generated by Django 4.1.3 on 2022-12-04 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_vacancy_maxage_vacancy_minage_vacancy_work_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='country',
            field=models.CharField(choices=[('POLAND', 'POLAND'), ('SERBIA', 'SERBIA'), ('SLOVAKIA', 'SLOVAKIA'), ('CROATIA', 'CROATIA')], max_length=250),
        ),
    ]
