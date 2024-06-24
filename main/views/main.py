from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from typing import Any
from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import AccessMixin
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.contrib.auth import logout

from main.models import Student, UserConnect, Grade, SClass


class MainView(TemplateView):
    def get(self, request):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login')) #to login page
        
        connector: UserConnect
        try:
            connector = UserConnect.objects.get(user=self.request.user.id)
        except UserConnect.DoesNotExist:
            logout(request)
            return HttpResponseRedirect(reverse_lazy('index'))
        
        match connector.utype:
            case UserConnect.STUD:
                return HttpResponseRedirect(reverse_lazy('student:main')) #to student page
            
            case UserConnect.TEACH:
                return HttpResponseRedirect(reverse_lazy('teacher:main')) #to teacher page
            
            case UserConnect.ADMIN:
                return HttpResponseRedirect(reverse_lazy('administrator:main')) #to admin page
            
            case _:
                logout(request)
                return HttpResponseRedirect(reverse_lazy('index'))
