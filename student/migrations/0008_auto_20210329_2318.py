# Generated by Django 3.1.7 on 2021-03-29 16:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20210329_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2021, 3, 29, 23, 18, 17, 831439)),
        ),
    ]