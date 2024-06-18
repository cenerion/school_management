from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = {
    'M': 'Male',
    'F': 'Female',
}


class UserConnect(models.Model):
    NONE = 0
    ADMIN = 1
    STUD = 2
    TEACH = 3

    USER_TYPE = {
        NONE: 'None',
        ADMIN: 'Administration',
        STUD: 'Student',
        TEACH: 'Teacher',
    }

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    utype = models.IntegerField(choices=USER_TYPE, default=NONE, null=False)
    other_id = models.BigIntegerField()

    def __str__(self) -> str:
        ret: str = f'{self.user} {self.utype} '

        if self.utype is self.STUD:
            stud = Student.objects.get(pk=self.other_id)
            ret += f'{stud}'
        elif self.utype is self.TEACH:
            teach = Teacher.objects.get(pk=self.other_id)
            ret += f'{teach}'

        return ret


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