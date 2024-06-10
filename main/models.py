from django.db import models


GENDER_CHOICES = {
        'M': 'Male',
        'F': 'Female',
}


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=100, null=False)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


class SClass(models.Model):
    profile = models.CharField(max_length=50, null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    symbol = models.CharField(max_length=5, null=False)


class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=100, null=False)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    sclass = models.ForeignKey(SClass, on_delete=models.PROTECT, null=True, blank=True)
    address = models.CharField(max_length=255)


class Subject(models.Model):
    name = models.CharField(max_length=50, null=False)


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    value = models.FloatField()
    name = models.CharField(max_length=50, null=False)
    date = models.DateField()