from django.urls import path

from main import views

urlpatterns = [
    path("", views.index, name="index"),
    path("uczniowie/list", views.UczniowieListView.as_view(), name='uczniowie'),
    path('uczniowie/create', views.UcznCreateView.as_view(), name='create ucz'),
    path('uczniowie/update/<pk>', views.UczniowieUpdate.as_view(), name='ucz update'),
]