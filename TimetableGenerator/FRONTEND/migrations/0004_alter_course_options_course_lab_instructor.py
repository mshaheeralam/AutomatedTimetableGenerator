# Generated by Django 4.0 on 2022-01-06 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FRONTEND', '0003_remove_course_type_course_lab'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-credithour']},
        ),
        migrations.AddField(
            model_name='course',
            name='lab_instructor',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
