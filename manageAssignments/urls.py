from django.urls import path

from . import views

urlpatterns=[

    path('AssignmentPage.html',views.AssignmentPage,name='AssignmentPage'),
    path('PutAssignmentData',views.putAssignmentData,name='putAssignmentData'),
    path('StudentHomePage.html',views.displayStudentAssignmentList,name='student_home'),

    path('TeacherHomePage.html',views.teacherHomePage,name='TeacherHomePage')
]

