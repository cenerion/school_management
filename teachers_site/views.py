from django.forms import BaseModelForm
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import AccessMixin
from django.db.models.query import QuerySet
from django.forms.widgets import DateInput
from django.urls import reverse_lazy

from main.models import UserConnect, Teacher, SClass, Student, Grade


class TeacherGenericMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if self.request.user.is_anonymous:
            return self.handle_no_permission()
        
        try:
            connector = UserConnect.objects.get(user=self.request.user.id)
            if connector.utype is not UserConnect.TEACH:
                return self.handle_no_permission()            
            self.teacher = Teacher.objects.get(pk=connector.other_id)
 
        except UserConnect.DoesNotExist:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self) -> HttpResponseRedirect:
        return HttpResponseRedirect(reverse_lazy('index'))


class TeacherMainView(TeacherGenericMixin, View):
    def get(self, request):
        return HttpResponseRedirect(reverse_lazy('teacher:class list'))


class ClassListView(TeacherGenericMixin, ListView):
    model=SClass
    context_object_name = 'class_list'
    template_name = 'teachers_site/class_list.html'


class ClassStudentListView(TeacherGenericMixin, ListView):
    model=Student
    context_object_name = 'students'
    template_name = 'teachers_site/students.html'

    def get_queryset(self) -> QuerySet[Student]:
        queryset = super().get_queryset()

        pk = self.kwargs.get('pk')
        if pk is not None:
            queryset = queryset.filter(sclass=pk)

        if pk is None:
            raise AttributeError(
                "View %s must be called with either an object pk in the URLconf." % self.__class__.__name__
            )

        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)

        return queryset


class StudentGradesListview(TeacherGenericMixin, ListView):
    model=Grade
    context_object_name = 'grades'
    template_name = 'teachers_site/grades.html'

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['s_pk'] = self.kwargs.get('pk')
        context['c_pk'] = Student.objects.get(pk=self.kwargs.get('pk')).sclass.pk
        return context

    def get_queryset(self) -> QuerySet[Grade]:
        queryset = super().get_queryset()

        pk = self.kwargs.get('pk')
        if pk is not None:
            queryset = queryset.filter(student=pk)

        if pk is None:
            raise AttributeError(
                "View %s must be called with either an object pk in the URLconf." % self.__class__.__name__
            )

        queryset = queryset.order_by('date', 'subject')
        return queryset


class AddGradeView(TeacherGenericMixin, CreateView):
    model = Grade
    template_name = 'teachers_site/form.html'
    template_name_suffix = '_create_form'
    fields = ['subject', 'value', 'name', 'date']

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['s_pk'] = self.kwargs.get('pk')
        return context

    def get_form(self, form_class: type[BaseModelForm] | None = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['date'].widget = DateInput(attrs={'type':'date'})
        return form
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object: Grade = form.save(commit=False)
        self.object.student = Student.objects.get(pk=self.kwargs.get('pk'))
        con = UserConnect.objects.get(user=self.request.user.pk)
        self.object.teacher = Teacher.objects.get(pk=con.other_id)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self) -> str:
        return reverse_lazy('teacher:grade list', kwargs={'pk': self.kwargs.get('pk')})


class ModifyGradeView(TeacherGenericMixin, UpdateView):
    model = Grade
    template_name = 'teachers_site/form.html'
    template_name_suffix = '_create_form'
    fields = ['subject', 'value', 'name', 'date']

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['s_pk'] = self.kwargs.get('s_pk')
        return context

    def get_form(self, form_class: type[BaseModelForm] | None = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['date'].widget = DateInput(attrs={'type':'date'})
        return form

    def get_success_url(self) -> str:
        return reverse_lazy('teacher:grade list', kwargs={'pk':  self.kwargs.get('s_pk')})
