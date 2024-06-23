from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin
from django.forms.widgets import DateInput
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from admin_site.apps import AdminSiteConfig

from admin_site.views.main import AdminGenericMixin
from main.models import Student, UserConnect

class StudentsSpecificClassView(ListView):
    model=Student
    template_name = 'admin_site/student_list.html'
    context_object_name = 'students'

    def get_queryset(self) -> QuerySet[Any]:
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

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["c_pk"] = self.kwargs.get('pk')
        return context
    

class StudentCreateView(CreateView):
    model = Student
    template_name = 'admin_site/student_create.html'
    fields = '__all__'

    def get_form(self, form_class: type[BaseModelForm] | None = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['birth_date'].widget = DateInput(attrs={'type':'date'})
        return form
    
    def create_username(self) -> str:
        stud = self.object
        ret: str = f'{stud.first_name[:4]}{stud.last_name[:4]}_'.lower().strip()

        similar_usernames:list = list( User.objects.filter(username__istartswith=ret).values_list('username', flat=True) )

        if similar_usernames:
            new_suffix = max( [int(u.split('_')[1]) for u in similar_usernames] ) + 1
            return f'{ret}{new_suffix}'
        
        return f'{ret}0'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object: Student = form.save()
        user = User.objects.create_user(self.create_username(), password=None)
        UserConnect.objects.create(user=user, utype=UserConnect.STUD, other_id=self.object.pk)
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["c_pk"] = self.kwargs.get('c_pk')
        return context
    
    def get_success_url(self) -> str:
        return reverse_lazy('administrator:student cred', kwargs={'pk':  self.object.pk, 'c_pk':  self.object.sclass.pk})
    

class StudentCredentialsView(TemplateView):
    template_name = 'admin_site/student_cred.html'

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
        context['c_pk'] = self.kwargs.get('c_pk')
        return context
    

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'admin_site/student_update.html'
    fields = '__all__'

    def get_form(self, form_class: BaseModelForm | None = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['birth_date'].widget = DateInput(attrs={'type':'date'})
        return form
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["c_pk"] = self.kwargs.get('c_pk')
        return context

    def get_success_url(self) -> str:
        return reverse_lazy('administrator:student list', kwargs={'pk':  self.object.sclass.pk})
    

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'admin_site/student_delete.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["c_pk"] = self.kwargs.get('c_pk')
        return context
    
    def form_valid(self, form):
        #self.c_pk = self.object.sclass.pk
        pk = self.object.pk
        try:
            connector = UserConnect.objects.filter(utype=UserConnect.STUD).get(other_id=pk)
            connector.user.delete()
        except UserConnect.DoesNotExist:
            pass
        finally:
            return super().form_valid(form)
        
    def get_success_url(self) -> str:
        return reverse_lazy('administrator:student list', kwargs={'pk':  self.kwargs.get('c_pk')})