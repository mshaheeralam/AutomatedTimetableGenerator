# Generated by Django 4.0 on 2022-01-03 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FRONTEND', '0002_course_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='type',
        ),
        migrations.AddField(
            model_name='course',
            name='lab',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
