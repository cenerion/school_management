from typing import Any
from django.forms import BaseModelForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.forms.widgets import DateInput
from django.urls import reverse_lazy

from admin_site.views.main import AdminGenericMixin
from main.models import SClass


class ClassListView(ListView):
    model=SClass
    template_name = 'admin_site/class_list.html'
    context_object_name = 'class_list'

    
class ClassCreateView(CreateView):
    model = SClass
    template_name = 'admin_site/class_create.html'
    fields = ['profile', 'teacher', 'symbol']
    success_url = reverse_lazy('administrator:class list')


class ClassUpdateView(UpdateView):
    model = SClass
    template_name = 'admin_site/class_update.html'
    fields = ['profile', 'teacher', 'symbol']
    success_url = reverse_lazy('administrator:class list')


class ClassDeleteView(DeleteView):
    model = SClass
    template_name = 'admin_site/class_delete.html'
    success_url = reverse_lazy('administrator:class list')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["c_pk"] = self.kwargs.get('c_pk')
        return context
        