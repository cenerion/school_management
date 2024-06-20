from django.contrib import admin
from main import models
# Register your models here.

admin.site.register(models.UserConnect)
admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.Grade)
admin.site.register(models.SClass)
admin.site.register(models.Subject)
#admin.site.register(models.)