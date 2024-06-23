from django.forms import BaseModelForm
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import AccessMixin
from django.db.models.query import QuerySet
from django.forms.widgets import DateInput
from django.urls import reverse_lazy

from main.models import UserConnect


class AdminGenericMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.is_anonymous:
            return self.handle_no_permission()

        try:
            connector = UserConnect.objects.get(user=self.request.user.id)
            if connector.utype is not UserConnect.ADMIN:
                return self.handle_no_permission()

        except UserConnect.DoesNotExist:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self) -> HttpResponseRedirect:
        return HttpResponseRedirect(reverse_lazy('index'))

class AdminMainView(TemplateView):
    template_name = 'admin_site/main.html'
