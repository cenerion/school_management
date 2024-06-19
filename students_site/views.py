from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth.mixins import AccessMixin
from django.db.models.query import QuerySet

from main.models import Student, UserConnect, Grade


class StudentGenericMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if self.request.user.is_anonymous:
            return self.handle_no_permission()
        
        try:
            connector = UserConnect.objects.get(user=self.request.user.id)
            if connector.utype is not UserConnect.STUD:
                return self.handle_no_permission()
            self.student = Student.objects.get(pk=connector.other_id)
        except UserConnect.DoesNotExist:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)


class MainView(StudentGenericMixin, View):
    def get(self, request):
        #return HttpResponse("Student main view")
        return render(request, 'students_site/main.html', None)
    

class GradeListView(StudentGenericMixin, ListView):
    model=Grade
    context_object_name = 'grades'

    def get_queryset(self) -> QuerySet[Grade]:
        queryset = super().get_queryset()
        queryset = queryset.filter(student=self.student.pk)
        queryset = queryset.order_by('date', 'subject')
        return queryset


class ClassStudentListView(StudentGenericMixin, ListView):
    model=Student
    context_object_name = 'grades'

    def get_queryset(self) -> QuerySet[Student]:
        queryset = super().get_queryset()
        queryset = queryset.filter(sclass=self.student.sclass)
        queryset = queryset.order_by('last_name', 'first_name')
        return queryset
