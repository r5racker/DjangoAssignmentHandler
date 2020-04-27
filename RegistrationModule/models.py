from django.db import models



class Courses(models.Model):
    c_id=models.CharField(max_length=10,primary_key=True)
    c_name=models.CharField(max_length=20)
    c_credit=models.DecimalField(decimal_places=2,max_digits=5)

class AppUsers(models.Model):
   user_email=models.CharField(max_length=50,primary_key=True)
   user_password=models.CharField(max_length=20)

class Student(models.Model):
    '''class for student db'''
    student_first_name=models.CharField(max_length=20)
    student_middle_name=models.CharField(max_length=20)
    student_last_name=models.CharField(max_length=20)
    
    
    student_dob=models.DateTimeField('date published')
    student_semester=models.IntegerField()
    
    student_email=models.CharField(max_length=50,primary_key=True)
    student_address=models.CharField(max_length=200)
    student_address2=models.CharField(max_length=200,default="NO_ADDR")
    student_city=models.CharField(max_length=20)
    student_state=models.CharField(max_length=20)
    student_zip=models.CharField(max_length=7)
    student_mobile_no=models.CharField(max_length=15)
    student_id_no=models.CharField(max_length=15)
    student_image=models.ImageField(upload_to='stu_pics',blank=True)
    models.DateTimeField()

# Create your models here.
class StudentCourse(models.Model):
    student_email=models.CharField(max_length=50)
    c_id=models.CharField(max_length=10)
    models.ForeignKey(Courses,on_delete=models.CASCADE)
    models.ForeignKey(Student,on_delete=models.CASCADE)
    class Meta:
        unique_together = ('student_email', 'c_id')

class Teacher(models.Model):
    '''db table for teachers'''
    teacher_first_name=models.CharField(max_length=20)
    teacher_middle_name=models.CharField(max_length=20)
    teacher_last_name=models.CharField(max_length=20)
    
    teacher_dob=models.DateTimeField('date published')
    
    teacher_email=models.CharField(max_length=50,primary_key=True)
    teacher_address=models.CharField(max_length=200)
    teacher_address2=models.CharField(max_length=200,default="NO_ADDR")
    teacher_city=models.CharField(max_length=20)
    teacher_state=models.CharField(max_length=20)
    teacher_zip=models.CharField(max_length=7)
    teacher_mobile_no=models.CharField(max_length=15)
    teacher_id_no=models.CharField(max_length=15)
    teacher_image=models.ImageField(upload_to='teacher_pics',blank=True)
    models.DateTimeField()
