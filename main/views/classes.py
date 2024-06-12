from django.forms import BaseModelForm
from django.views.generic import ListView, CreateView, UpdateView
from django.forms.widgets import DateInput
from django.urls import reverse_lazy

from main.models import SClass


class ClassListView(ListView):
    model=SClass
    context_object_name = 'class_list'

    
class ClassCreateView(CreateView):
    model = SClass
    template_name_suffix = '_create_form'
    fields = ['profile', 'teacher', 'symbol']
    success_url = reverse_lazy('class list')


class ClassUpdate(UpdateView):
    model = SClass
    template_name_suffix = '_update_form'
    fields = ['profile', 'teacher', 'symbol']
    success_url = reverse_lazy('class list')
