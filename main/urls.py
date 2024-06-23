from django.urls import path

from main.views import main, account

urlpatterns = [
    path("", main.MainView.as_view(), name="index"),
    path('login', account.MyLoginView.as_view(), name='login'),
    path('logout', account.MyLogoutView.as_view(), name='logout'),
]