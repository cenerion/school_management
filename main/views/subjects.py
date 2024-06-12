from django.forms import BaseModelForm
from django.views.generic import ListView, CreateView, UpdateView
from django.forms.widgets import DateInput
from django.urls import reverse_lazy

from main.models import Subject


class SubjectListView(ListView):
    model=Subject
    context_object_name = 'subject_list'


class SubjectCreateView(CreateView):
    model = Subject
    template_name_suffix = '_create_form'
    fields = ['name']
    success_url = reverse_lazy('subject list')


class SubjectUpdate(UpdateView):
    model = Subject
    template_name_suffix = '_update_form'
    fields = ['name']
    success_url = reverse_lazy('subject list')
