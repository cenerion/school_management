from django.forms import BaseModelForm
from django.views.generic import ListView, CreateView, UpdateView
from django.forms.widgets import DateInput
from django.urls import reverse_lazy

from main.models import Teacher


class TeacherListView(ListView):
    model=Teacher
    context_object_name = 'teachers'

    
class TeacherCreateView(CreateView):
    model = Teacher
    template_name_suffix = '_create_form'
    fields = ['first_name', 'last_name', 'birth_date', 'gender']
    success_url = reverse_lazy('teacher list')

    def get_form(self, form_class: type[BaseModelForm] | None = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['birth_date'].widget = DateInput(attrs={'type':'date'})
        return form


class TeacherUpdate(UpdateView):
    model = Teacher
    template_name_suffix = '_update_form'
    fields = ['first_name', 'last_name', 'birth_date', 'gender']
    success_url = reverse_lazy('teacher list')

    def get_form(self, form_class: BaseModelForm | None = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['birth_date'].widget = DateInput(attrs={'type':'date'})
        return form
    