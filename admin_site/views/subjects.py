from django.forms import BaseModelForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.forms.widgets import DateInput
from django.urls import reverse_lazy

from admin_site.views.main import AdminGenericMixin
from main.models import Subject


class SubjectListView(ListView):
    model=Subject
    template_name = 'admin_site/subject_list.html'
    context_object_name = 'subject_list'


class SubjectCreateView(CreateView):
    model = Subject
    template_name = 'admin_site/subject_create.html'
    fields = ['name']
    success_url = reverse_lazy('administrator:subject list')


class SubjectUpdateView(UpdateView):
    model = Subject
    template_name = 'admin_site/subject_update.html'
    fields = ['name']
    success_url = reverse_lazy('administrator:subject list')


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'admin_site/subject_delete.html'
    success_url = reverse_lazy('administrator:subject list')
