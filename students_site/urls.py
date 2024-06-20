from django.urls import path
from students_site.views import MainView, GradeListView, ClassStudentListView

urlpatterns = [
    path("", MainView.as_view(), name='main'),
    path("grades/", GradeListView.as_view(), name='grade list'),
    path("class/", ClassStudentListView.as_view(), name='class'),
]
