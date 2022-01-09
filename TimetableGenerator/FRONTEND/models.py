from django.db import models


# Create your models here.


class Course(models.Model):
    faculty_choices = [
        ('FCSE', 'FCSE'),
        ('FME', 'FME'),
        ('FEE', 'FEE'),
        ('FES', 'FES'),
        ('FMCE', 'FMCE'),
        ('MGS', 'MGS')
    ]
    code = models.CharField(max_length=10, primary_key=True)
    instructor = models.CharField(max_length=50)
    time = models.DateTimeField(null=True, blank=True)
    group = models.CharField(max_length=50)
    credithour = models.IntegerField(default=0, blank=True, null=True)
    faculty = models.CharField(max_length=4, choices=faculty_choices)
    lab = models.BooleanField()
    lab_instructor = models.CharField(max_length=50, null=True, blank=True)
    lab_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-lab']

    def __str__(self):
        return self.code


"""
class CourseType(models.Model):
    course_type = [
        ('Theory', 'Theory'),
        ('Lab', 'Lab')
    ]
    type = models.CharField(max_length=200, null=True, choices=course_type)

class Student(models.Model):
    name = models.CharField(max_length=50)
    reg = models.IntegerField(primary_key=True)
    degree_choices = [
        ('BCS', 'BCS'),
        ('BCE', 'BCE'),
        ('BME', 'BME'),
        ('BEE', 'BEE'),
        ('BES', 'BES'),
        ('BCVE', 'BCVE'),
        ('BMGS', 'BMGS'),
        ('BAI', 'BAI'),
        ('BDS', 'BDS')
    ]
    degree = models.CharField(max_length=4,choices=degree_choices, default="")
    # batch = "{{reg[0:3] - 1990}}" + name[1:]

    def __str__(self):
        return self.name


class Teacher(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
"""
