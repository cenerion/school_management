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

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class SClass(models.Model):
    profile = models.CharField(max_length=50, null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    symbol = models.CharField(max_length=5, null=False)

    def __str__(self):
        return str(self.symbol) + " " + str(self.profile)


class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=100, null=False)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    sclass = models.ForeignKey(SClass, on_delete=models.PROTECT, null=True, blank=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


class Subject(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return str(self.name)


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    value = models.FloatField()
    name = models.CharField(max_length=50, null=False)
    date = models.DateField()

    def __str__(self):
        return str(self.value)