from django.forms import BaseModelForm
from django.views.generic import ListView, CreateView, UpdateView
from django.forms.widgets import DateInput
from django.urls import reverse_lazy

from main.models import Grade


class GradeListView(ListView):
    model=Grade
    context_object_name = 'grades'

    
class GradeCreateView(CreateView):
    model = Grade
    template_name_suffix = '_create_form'
    fields = ['student', 'teacher', 'subject',
              'value', 'name', 'date']
    success_url = reverse_lazy('grade list')

    def get_form(self, form_class: type[BaseModelForm] | None = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['date'].widget = DateInput(attrs={'type':'date'})
        return form


class GradeUpdate(UpdateView):
    model = Grade
    template_name_suffix = '_create_form'
    fields = ['student', 'teacher', 'subject',
              'value', 'name', 'date']
    success_url = reverse_lazy('grade list')

    def get_form(self, form_class: type[BaseModelForm] | None = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['date'].widget = DateInput(attrs={'type':'date'})
        return form
    