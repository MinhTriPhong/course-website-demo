# Generated by Django 3.1.7 on 2021-03-29 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20210329_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.DecimalField(decimal_places=0, default=2844, max_digits=4),
        ),
    ]
