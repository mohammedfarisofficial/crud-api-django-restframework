from django.urls import path

from api.models import Student
from . import views

urlpatterns=[
     path('',views.studentsList,name='student-list'),
     path('student/<str:pk>/',views.studentDetails,name='student-details'),
     path('student_add/',views.studentAdd,name='add-student'),
     path('student_update/<int:pk>/',views.studentUpdate,name='student-update'),
     path('student_delete/<int:pk>/',views.studentDelete,name='student-delete')
]
