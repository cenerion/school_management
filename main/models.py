from django.db import models
from django.db.models.signals import pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver


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
    other_id = models.BigIntegerField(blank=True)

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

@receiver(pre_delete, sender=Teacher)
def teacher_remove_account(sender, instance, **kwargs):
    pk = instance.pk
    try:
        connector = UserConnect.objects.filter(utype=UserConnect.TEACH).get(other_id=pk)
        connector.user.delete()
    except UserConnect.DoesNotExist:
        pass


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
    sclass = models.ForeignKey(SClass, on_delete=models.CASCADE, null=False)
    address = models.CharField(max_length=255)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

@receiver(pre_delete, sender=Student)
def student_remove_account(sender, instance, **kwargs):
    pk = instance.pk
    try:
        connector = UserConnect.objects.filter(utype=UserConnect.STUD).get(other_id=pk)
        connector.user.delete()
    except UserConnect.DoesNotExist:
        pass


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