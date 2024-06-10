from django.http import HttpRequest, HttpResponse
from django.forms import BaseModelForm
from django.views.generic import ListView, CreateView, UpdateView
from django.forms.widgets import DateInput
from django.urls import reverse_lazy

from main.models import Uczen


class UczniowieListView(ListView):
    model=Uczen
    context_object_name = 'students'
    
    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'lista uczniów'
        return context

    
class UcznCreateView(CreateView):
    model = Uczen
    template_name_suffix = '_create_form'
    fields = ['imie', 'nazwisko', 'data_ur',
              'plec', 'klasa', 'adres_zam']
    success_url = reverse_lazy('uczniowie')

    def get_form(self, form_class: type[BaseModelForm] | None = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['data_ur'].widget = DateInput(attrs={'type':'date'})
        return form


class UczniowieUpdate(UpdateView):
    model = Uczen
    template_name_suffix = '_update_form'
    fields = ['imie', 'nazwisko', 'data_ur',
              'plec', 'klasa', 'adres_zam']
    success_url = reverse_lazy('uczniowie')

    def get_form(self, form_class: BaseModelForm | None = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['data_ur'].widget = DateInput(attrs={'type':'date'})
        return form
    