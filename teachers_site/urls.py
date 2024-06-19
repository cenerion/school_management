from django.urls import path
from teachers_site import views

urlpatterns = [
    path("", views.TeacherMainView.as_view(), name='main'),
    path('class/', views.ClassListView.as_view(), name='class list'),
    path('class/<pk>', views.ClassStudentListView.as_view(), name='student list'),
    path('student/<pk>', views.StudentGradesListview.as_view(), name='grade list'),
    path('student/<pk>/grade/new', views.AddGradeView.as_view(), name='grade new'),
    path('student/<int:spk>/grade/<pk>', views.ModifyGradeView.as_view(), name='grade mod'),
]