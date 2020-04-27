from django.urls import path

from . import views

urlpatterns=[
    path('SubmissionPage.html',views.submissionPage,name='submission_page'),
    path('addSubmission',views.addSubmission,name='addSubmission'),
    path('removeSubmission',views.removeSubmission,name='removeSubmission'),
    path('SetSubmissionMarks',views.setSubmissionMarks,name='setSubmissionMarks'),
    path('StudentSubmissionDisplay.html',views.studentSubmissionDisplay,name='StudentSubmissionDisplay'),
    path('StudentViewSubmissionFile.html',views.studentViewSubmissionFile,name='student_view_submission_file'),
    path('ViewSubmissionFile.html',views.viewSubmissionFile,name='view_submission_file'),
    path('TeacherSubmissionDisplay.html',views.teacherSubmissionDisplay,name='TeacherAssignmentDisplay'),

    path('TeacherViewAllStudents.html',views.teacherViewAllStudents,name='teacherViewAllStudents'),
    path('ViewAllSubmissions.html',views.viewAllSubmissions,name='viewAllSubmissions'),
]