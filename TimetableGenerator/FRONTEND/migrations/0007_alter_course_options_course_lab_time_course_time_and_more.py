# Generated by Django 4.0 on 2022-01-06 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FRONTEND', '0006_alter_course_lab_instructor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-lab']},
        ),
        migrations.AddField(
            model_name='course',
            name='lab_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='faculty',
            field=models.CharField(choices=[('FCSE', 'FCSE'), ('FME', 'FME'), ('FEE', 'FEE'), ('FES', 'FES'), ('FMCE', 'FMCE'), ('MGS', 'MGS')], max_length=4),
        ),
    ]
