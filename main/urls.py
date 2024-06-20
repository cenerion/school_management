from django.urls import path

from main.views import main
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", main.MainView.as_view(), name="index"),
    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(), name='logout'),
]