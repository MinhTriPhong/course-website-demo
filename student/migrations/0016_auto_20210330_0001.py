# Generated by Django 3.1.7 on 2021-03-29 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_auto_20210330_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2021, 3, 30, 0, 1, 30, 188598)),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.DecimalField(decimal_places=0, default=44207, max_digits=6),
        ),
    ]
