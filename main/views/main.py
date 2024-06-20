from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from typing import Any
from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import AccessMixin
from django.db.models.query import QuerySet
from django.urls import reverse_lazy

from main.models import Student, UserConnect, Grade, SClass


class MainView(TemplateView):
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context[''] = ''
        return context
    
    def get(self, request):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('')) #to login page
        
        connector: UserConnect
        try:
            connector = UserConnect.objects.get(user=self.request.user.id)
        except UserConnect.DoesNotExist:
            return HttpResponseRedirect(reverse_lazy('')) # logout
        
        match connector.utype:
            case UserConnect.STUD:
                return HttpResponseRedirect(reverse_lazy('student:main')) #to student page
            
            case UserConnect.TEACH:
                return HttpResponseRedirect(reverse_lazy('teacher:main')) #to teacher page
            
            case UserConnect.ADMIN:
                return HttpResponseRedirect(reverse_lazy('')) #to admin page
            
            case _:
                return HttpResponseRedirect(reverse_lazy('')) # logout
