# Generated by Django 3.1.7 on 2021-03-28 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.TextField(),
        ),
    ]
