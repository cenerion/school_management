from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.forms.widgets import DateInput
from django.urls import reverse_lazy

from main.models import Student


class StudentListView(ListView):
    model=Student
    context_object_name = 'students'


class StudentsSpecificClassView(ListView):
    model=Student
    context_object_name = 'students'

    def get_queryset(self) -> QuerySet[any]:
        queryset = super().get_queryset()

        pk = self.kwargs.get('pk')
        if pk is not None:
            queryset = queryset.filter(sclass=pk)

        if pk is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )

        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)

        return queryset
    
    
class StudentCreateView(CreateView):
    model = Student
    template_name_suffix = '_create_form'
    fields = ['first_name', 'last_name', 'birth_date',
              'gender', 'sclass', 'address']
    success_url = reverse_lazy('student list')

    def get_form(self, form_class: type[BaseModelForm] | None = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['birth_date'].widget = DateInput(attrs={'type':'date'})
        return form


class StudentUpdate(UpdateView):
    model = Student
    template_name_suffix = '_update_form'
    fields = ['first_name', 'last_name', 'birth_date',
              'gender', 'sclass', 'address']
    success_url = reverse_lazy('student list')

    def get_form(self, form_class: BaseModelForm | None = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['birth_date'].widget = DateInput(attrs={'type':'date'})
        return form
    