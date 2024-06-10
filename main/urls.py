from django.urls import path

from main.views import main, students

urlpatterns = [
    path("", main.index, name="index"),
    path("student/list", students.StudentListView.as_view(), name='student list'),
    path('student/create', students.StudentCreateView.as_view(), name='student create'),
    path('student/update/<pk>', students.StudentUpdate.as_view(), name='student update'),
]