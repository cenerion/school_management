from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.forms.widgets import DateInput
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from main.models import Student, UserConnect


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
    fields = '__all__'
    success_url = reverse_lazy('student list')

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


class StudentUpdate(UpdateView):
    model = Student
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = reverse_lazy('student list')

    def get_form(self, form_class: BaseModelForm | None = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['birth_date'].widget = DateInput(attrs={'type':'date'})
        return form
    