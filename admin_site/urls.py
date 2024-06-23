from django.urls import path
from admin_site.views import teachers, subjects, classes, students, main

urlpatterns = [
    path("", main.AdminMainView.as_view(), name='main'),

    path("teacher/", teachers.TeacherListView.as_view(), name='teacher list'),
    path('teacher/new', teachers.TeacherCreateView.as_view(), name='teacher new'),
    path('teacher/<pk>', teachers.TeacherUpdateView.as_view(), name='teacher mod'),
    path('teacher/<pk>/cred', teachers.TeacherCredentialsView.as_view(), name='teacher cred'),
    path('teacher/<pk>/delete', teachers.TeacherDeleteView.as_view(), name='teacher del'),
    
    path("subject/", subjects.SubjectListView.as_view(), name='subject list'),
    path('subject/new', subjects.SubjectCreateView.as_view(), name='subject new'),
    path('subject/<pk>', subjects.SubjectUpdateView.as_view(), name='subject mod'),
    path('subject/<pk>/delete', subjects.SubjectDeleteView.as_view(), name='subject del'),

    path('class/', classes.ClassListView.as_view(), name='class list'),
    path('class/new', classes.ClassCreateView.as_view(), name='class new'),
    path('class/<pk>', classes.ClassUpdateView.as_view(), name='class mod'),
    path('class/<pk>/delete', classes.ClassDeleteView.as_view(), name='class del'),

    path('class/<pk>/list', students.StudentsSpecificClassView.as_view(), name='student list'),
    path('student/<int:c_pk>/new', students.StudentCreateView.as_view(), name='student new'),
    path('student/<int:c_pk>/<pk>/cred', students.StudentCredentialsView.as_view(), name='student cred'),
    path('student/<int:c_pk>/<pk>', students.StudentUpdateView.as_view(), name='student mod'),
    path('student/<int:c_pk>/<pk>/delete', students.StudentDeleteView.as_view(), name='student del'),
]