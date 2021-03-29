# Generated by Django 3.1.7 on 2021-03-29 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_name', models.TextField()),
                ('Lecture_name', models.TextField()),
                ('Duration', models.DecimalField(decimal_places=1, default=11, max_digits=3)),
            ],
        ),
    ]
