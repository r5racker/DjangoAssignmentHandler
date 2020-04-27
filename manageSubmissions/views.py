from django.shortcuts import render

import os
from django.contrib import messages
from manageAssignments.models import Assignment
import datetime
from django.db import models
from django.http import HttpResponseRedirect
from RegistrationModule.models import StudentCourse,Student,Courses
from django.template.context_processors import csrf
from manageSubmissions.models import Submission
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.decorators import login_required

def addSubmission(request):
    if request.user.is_authenticated:
        if True:
            
            
            t_assign_id=int(request.POST.get('student_assignment_id'))
            t_student_email=request.POST.get('student_submission_email')
            t_submission_date=datetime.datetime.now()
            t_submission_file_name=request.FILES['student_file']
            t_c_id=Assignment.objects.get(assign_id=t_assign_id).c_id

            sub=Submission(assign_id=t_assign_id,student_email=t_student_email,submission_date=t_submission_date,submission_file_name=t_submission_file_name,submission_c_id=t_c_id)
            sub.save()
            mssg="The file is uploaded successfully!!"
        else:
            mssg="No file uploaded"
        return HttpResponseRedirect('SubmissionPage.html',messages.success(request,mssg))
    else:
        return HttpResponseRedirect('/',{'message':'Please Login'})    


def removeSubmission(request):
    if request.user.is_authenticated:
        t_assign_id=request.GET.get('assign_id')
        sub=Submission.objects.get(assign_id=t_assign_id,student_email=request.user.username)
        sub.delete()
        return HttpResponseRedirect('StudentSubmissionDisplay.html')
    else:
        return HttpResponseRedirect('/',{'message':'Please Login'})

#@login_required(login_url='')
def submissionPage(request):
    
    if request.user.is_authenticated:
        try:
            student_course=StudentCourse.objects.filter(student_email=request.user.username)
            student_submitted_ass=Submission.objects.filter(student_email=request.user.username)
            student_submitted_ass_id=[ass.assign_id for ass in student_submitted_ass]

            
            ass_id_list=[]
            home_ass_id=None
            if request.GET.get('assign_id'):
                home_ass_id=int(request.GET.get('assign_id'))
                
            for course in student_course:
                all_assign=Assignment.objects.filter(c_id=course.c_id).filter(assign_due_date__gte=datetime.date.today())
                for temp_ass in all_assign:
                    if temp_ass.assign_id not in student_submitted_ass_id:
                        ass_id_list.append(temp_ass)
            
        except Student.DoesNotExist:
            ass_id_list = None
        c={'ass_list':ass_id_list,'student_email':request.user.username,'ass_id':home_ass_id}
        c.update(csrf(request))
        return render(request,'SubmissionPage.html',c)
    else:
        return HttpResponseRedirect('/',{'message':'Please Login'})

def studentSubmissionDisplay(request):
    if request.user.is_authenticated:
        c={}
        
        course_list=Courses.objects.all()
        enrolled_list=StudentCourse.objects.filter(student_email=request.user.username)
        enrolled_id_list=[c.c_id for c in enrolled_list]
        c['sub_list']=Submission.objects.filter(student_email=request.user.username)
        s_course_list=[c for c in course_list if c.c_id in enrolled_id_list]
        c['course_list']=s_course_list
        
        if request.method=='POST' and request.POST.get("student_course_id")!="0":
            
            t_course_id=request.POST.get("student_course_id")
            c['course_option']=t_course_id
            sub_list=Submission.objects.filter(submission_c_id=t_course_id)
            c['sub_list']=sub_list
            
        c.update(csrf(request))
        return render(request,'StudentSubmissionDisplay.html',c)
    else:
        return HttpResponseRedirect('/')

def studentViewSubmissionFile(request):
    if request.user.is_authenticated:
        c={}
        try:
            t_stu_email=request.user.username
            t_assign_id=request.GET.get("assign_id")
            
            file_url=Submission.objects.get(student_email=t_stu_email,assign_id=t_assign_id).submission_file_name.url
            
            file_name=file_url.split('/')
            file_name.reverse()
            c['file_name']=file_name[0]
            f = open(os.path.dirname(__file__)+'\\..\\media\\'+file_name[1]+'\\'+file_name[0], 'r')
            
            c['file_content']=f.read()
            c['stu_email']=t_stu_email
            c['assign_id']=t_assign_id
        except Submission.DoesNotExist:
            print("MyError: At manageSubmissioin.views.viewSubmissionFile() try block ")
        c.update(csrf(request))
        return render(request,'StudentViewSubmissionFile.html',c)

    else:
        return HttpResponseRedirect('/')




#@xframe_options_exempt
def viewSubmissionFile(request):
    if request.user.is_authenticated:
        c={}
        try:
            t_stu_email=request.GET.get("stu_email")
            t_assign_id=request.GET.get("assign_id")
            
            file_url=Submission.objects.get(student_email=t_stu_email,assign_id=t_assign_id).submission_file_name.url
            
            file_name=file_url.split('/')
            file_name.reverse()
            c['file_name']=file_name[0]
            f = open(os.path.dirname(__file__)+'\\..\\media\\'+file_name[1]+'\\'+file_name[0], 'r')
            
            c['file_content']=f.read()
            c['stu_email']=t_stu_email
            c['assign_id']=t_assign_id
        except Submission.DoesNotExist:
            print("MyError: At manageSubmissioin.views.viewSubmissionFile() try block ")
        c.update(csrf(request))
        return render(request,'ViewSubmissionFile.html',c)

    else:
        return HttpResponseRedirect('/')


def teacherSubmissionDisplay(request):
    #list of assignments created by the logged in teacher
    if request.user.is_authenticated:
        c={}
        
        course_list=Courses.objects.all()
        c['course_list']=course_list
        sub_list_unmarked=[]
        sub_list_marked=[]
        
        if request.method =="GET" and request.GET.get("teacher_course_id")!=None and  request.GET.get("teacher_course_id")!="0":
            
            t_course_id=request.GET.get("teacher_course_id")
            c['course_option']=t_course_id
            
            ass_list=Assignment.objects.filter(c_id=t_course_id).filter(teacher_email=request.user.username)
            c['ass_list']=ass_list
            
            if request.GET.get("teacher_assignment_id") != None and request.GET.get("teacher_assignment_id")!=None and request.GET.get("teacher_assignment_id")!='0':
                
                c['assign_option']=int(request.GET.get("teacher_assignment_id")) ##beware of the data types
                '''print("{}=={}".format(type(ass_list[0].assign_id),type(request.GET.get("teacher_assignment_id"))))'''
                sub_list=Submission.objects.filter(assign_id=int(request.GET.get("teacher_assignment_id")))
                
                
                
                for sub in sub_list:
                    if(sub.submission_marks_logic==None):
                        sub_list_unmarked.append(sub)
                    else:
                        sub_list_marked.append(sub)
                
                c['sub_list_unmarked']=sub_list_unmarked
                c['sub_list_marked']=sub_list_marked
            else:
                ass_list=Assignment.objects.filter(teacher_email=request.user.username).order_by('c_id')
                ass_id_list=[a.assign_id for a in ass_list]
                sub_list=Submission.objects.filter(submission_c_id=t_course_id).order_by('submission_c_id')
                
                
                for sub in sub_list:
                    if sub.assign_id in ass_id_list and sub.submission_marks_logic==None:
                        sub_list_unmarked.append(sub)
                    else:
                        sub_list_marked.append(sub)
                c['sub_list_unmarked']=sub_list_unmarked
                c['sub_list_marked']=sub_list_marked
        else:
            ass_list=Assignment.objects.filter(teacher_email=request.user.username).order_by('c_id')
            ass_id_list=[a.assign_id for a in ass_list]
            sub_list=Submission.objects.order_by('submission_c_id')
            
            for sub in sub_list:
                if sub.assign_id in ass_id_list and sub.submission_marks_logic==None:
                    sub_list_unmarked.append(sub)
                else:
                    sub_list_marked.append(sub)
            c['sub_list_unmarked']=sub_list_unmarked
            c['sub_list_marked']=sub_list_marked
                
        c.update(csrf(request))
        return render(request,"TeacherSubmissionDisplay.html",c)            
    else:
        return HttpResponseRedirect('/')


def setSubmissionMarks(request):
    
    t_stu_email=request.POST.get('student_email')
    t_assign_id=request.POST.get('assign_id')
    t_mk_l=request.POST.get('submission_marks_logic')
    t_mk_u=request.POST.get('submission_marks_uniqueness')
    t_mk_q=request.POST.get('submission_marks_quality')
    try:
        sub=Submission.objects.get(student_email=t_stu_email,assign_id=t_assign_id)
        sub.submission_marks_logic=t_mk_l
        sub.submission_marks_uniqueness=t_mk_u
        sub.submission_marks_quality=t_mk_q
        sub.save()
    except Submission.DoesNotExist:
        print('Error at manageSubmission.setSubmission():submission not found')
        print(t_assign_id)
        print(t_stu_email)
        
    return HttpResponseRedirect("TeacherSubmissionDisplay.html")

def teacherViewAllStudents(request):
    if request.user.is_authenticated:
        c={}
        stu_list=Student.objects.all()
        c['stu_list']=stu_list
        
        return render(request,'TeacherViewAllStudents.html',c)
    else:
        return HttpResponseRedirect('/')

def viewAllSubmissions(request):
    if request.user.is_authenticated:
        c={}
        stu_email=request.GET.get('student_email')
        sub_list=Submission.objects.filter(student_email=stu_email)
        print(sub_list)
        c['sub_list']=sub_list
        
        return render(request,'ViewAllSubmissions.html',c)
    else:
        return HttpResponseRedirect('/')