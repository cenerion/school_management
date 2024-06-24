from django.urls import path

from main.views import main, account

urlpatterns = [
    path("", main.MainView.as_view(), name="index"),
    path('login', account.LoginView.as_view(), name='login'),
    path('logout', account.LogoutView.as_view(), name='logout'),
    path('pass_change', account.PasswordChangeView.as_view(), name='password change'),
]