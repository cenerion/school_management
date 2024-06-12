from django.urls import path

from main.views import main, students, classes

urlpatterns = [
    path("", main.index, name="index"),
    path("student/list", students.StudentListView.as_view(), name='student list'),
    path('student/create', students.StudentCreateView.as_view(), name='student create'),
    path('student/update/<pk>', students.StudentUpdate.as_view(), name='student update'),
    
    path("class/list", classes.ClassListView.as_view(), name='class list'),
    path('class/create', classes.ClassCreateView.as_view(), name='class create'),
    path('class/update/<pk>', classes.ClassUpdate.as_view(), name='class update'),
]