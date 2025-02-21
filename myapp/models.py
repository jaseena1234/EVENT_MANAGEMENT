from django.db import models

# Create your models here.
class LoginModel(models.Model):
    username = models.CharField(max_length=100, null=True,blank=True)
    password = models.CharField(max_length=100, null=True,blank=True)
    user_type = models.CharField(max_length=100, null=True,blank=True)

class DepartmentModel(models.Model):
    departmentname = models.CharField(max_length=100, null=True,blank=True)

class teacherModel(models.Model):
    LOGIN_ID = models.ForeignKey(LoginModel, on_delete=models.CASCADE, null=True,blank=True)
    teachername = models.CharField(max_length=100, null=True,blank=True)
    departmentname = models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, null=True,blank=True)
    contact = models.IntegerField(null=True,blank=True)

class EventModel(models.Model):
    Teacher_id = models.ForeignKey(teacherModel, on_delete=models.CASCADE, null = True, blank = True)
    DEPT_ID = models.ForeignKey(DepartmentModel,on_delete=models.CASCADE,null = True,blank =True)
    eventname = models.CharField(max_length=100, null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    eventCATAGORY =models.CharField(max_length=100, null=True,blank=True)
    time = models.TimeField(max_length=100, null=True,blank=True)
    numberofParticipant = models.IntegerField( null=True,blank=True)
    eventposter = models.ImageField(upload_to='eventposter/', null=True,blank=True)








class Teacher_Report(models.Model):
    TEACHERID=models.ForeignKey(teacherModel, on_delete=models.CASCADE, null=True,blank=True)
    cateogory=models.CharField(max_length=100, null=True,blank=True)
    name = models.CharField(max_length=100, null=True,blank=True)
    description = models.CharField(max_length=100, null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    venue = models.CharField(max_length=100, null=True,blank=True)
    certificate = models.ImageField(upload_to='certificate/',null=True,blank=True)

class studentModel(models.Model):
    studentname = models.CharField(max_length=100, null=True,blank=True)
    DEPARTMENT = models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, null=True,blank=True)
    contact = models.IntegerField(null=True,blank=True)
    admissionnumber = models.IntegerField(null=True,blank=True)


class Student_Report(models.Model):
    STUDENTID=models.ForeignKey(studentModel, on_delete=models.CASCADE, null=True,blank=True) 
    cateogory=models.CharField(max_length=100, null=True,blank=True)
    name = models.CharField(max_length=100, null=True,blank=True)
    description = models.CharField(max_length=100, null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    venue = models.CharField(max_length=100, null=True,blank=True)
    certificate = models.ImageField(upload_to='certificate/',null=True,blank=True)   
    


class complaintModel(models.Model):
    complaint = models.CharField(max_length=100, null=True,blank=True)
    reply=models.ForeignKey(studentModel,on_delete=models.CASCADE)
    date = models.DateField(null=True,blank=True)


class notificationModel(models.Model):
    date = models.DateField(null=True,blank=True)
    notification = models.CharField(max_length=100, null=True,blank=True)


class resultModel(models.Model):
    date = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=100, null=True,blank=True)
    studentID = models.ForeignKey(studentModel,on_delete=models.CASCADE) 
    event = models.ForeignKey(EventModel,on_delete=models.CASCADE)


class reportModel(models.Model):
    status = models.CharField(max_length=100, null=True,blank=True) 
    event = models.ForeignKey(EventModel,on_delete=models.CASCADE)
    file = models.FileField(upload_to='report/',null=True,blank=True)           