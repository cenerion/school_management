from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from typing import Any
from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import AccessMixin
from django.db.models.query import QuerySet
from django.urls import reverse_lazy

from main.models import Student, UserConnect, Grade, SClass
from django.contrib.auth.views import LoginView, LogoutView

class MyLoginView(LoginView):
    redirect_authenticated_user=True
    def get_success_url(self) -> str:
        return reverse_lazy('index')

class MyLogoutView(LogoutView):
    def get_success_url(self) -> str:
        return reverse_lazy('index')
