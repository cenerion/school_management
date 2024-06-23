from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.forms.widgets import DateInput
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from admin_site.apps import AdminSiteConfig
from django.views.generic.base import TemplateView

from main.models import Teacher, UserConnect
from admin_site.views.main import AdminGenericMixin


class TeacherListView(ListView):
    model=Teacher
    template_name = 'admin_site/teacher_list.html'
    context_object_name = 'teacher_list'


class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'admin_site/teacher_create.html'
    fields = '__all__'
    success_url = reverse_lazy('administrator:teacher list')

    def get_form(self, form_class: type[BaseModelForm] | None = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['birth_date'].widget = DateInput(attrs={'type':'date'})
        return form
    
    def create_username(self) -> str:
        teach = self.object
        ret: str = f'{teach.first_name[:4]}{teach.last_name[:4]}_'.lower().strip()

        similar_usernames:list = list( User.objects.filter(username__istartswith=ret).values_list('username', flat=True) )

        if similar_usernames:
            new_suffix = max( [int(u.split('_')[1]) for u in similar_usernames] ) + 1
            return f'{ret}{new_suffix}'
        
        return f'{ret}0'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object: Teacher = form.save()
        user = User.objects.create_user(self.create_username(), password=None)
        UserConnect.objects.create(user=user, utype=UserConnect.TEACH, other_id=self.object.pk)
        return HttpResponseRedirect(self.get_success_url())


    def get_success_url(self) -> str:
        return reverse_lazy('administrator:teacher cred', kwargs={'pk':  self.object.pk})
    

class TeacherCredentialsView(TemplateView):
    template_name = 'admin_site/teacher_cred.html'

    def generate_password(self):
        pk = self.kwargs.get('pk')
        connector = UserConnect.objects.get(other_id=pk)
        user = connector.user

        password = get_random_string(10, AdminSiteConfig.acceptable_password_chars)
        user.set_password(password)

        user.save()
        return user.username, password

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        u, p = self.generate_password()
        context['username'] = u
        context["pass"] = p
        return context
    



class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'admin_site/teacher_update.html'
    fields = '__all__'
    success_url = reverse_lazy('administrator:teacher list')

    def get_form(self, form_class: BaseModelForm | None = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['birth_date'].widget = DateInput(attrs={'type':'date'})
        return form
   

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'admin_site/teacher_delete.html'
    success_url = reverse_lazy('administrator:teacher list')
    