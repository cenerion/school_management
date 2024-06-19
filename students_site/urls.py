from django.urls import path
from students_site.views import MainView, GradeListView, ClassStudentListView

urlpatterns = [
    path("main/", MainView.as_view(), name='stud main'),
    path("grades/", GradeListView.as_view(), name='grade list'),
    path("class/", ClassStudentListView.as_view(), name='class'),
]
