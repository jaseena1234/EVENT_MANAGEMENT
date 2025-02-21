from dataclasses import fields
from django.forms import ModelForm


from .models import *


class EventModelForm(ModelForm):
    class Meta:
        model = EventModel
        fields = ['Teacher_id','DEPT_ID','eventname','date','eventCATAGORY','time','numberofParticipant','eventposter']
        
class Department_form(ModelForm):
    class Meta:
        model =DepartmentModel
        fields =['departmentname'] 

class teacherModelForm(ModelForm):
    class Meta:
        model =teacherModel
        fields=['teachername','departmentname','email','contact']
class  Teacher_ReportModelForm(ModelForm):
    class meta:
        model =Teacher_Report
        fields =['TEACHERID','cateogory','name','description','date','venue','certificate']
class studentModelForm(ModelForm):
    class meta:
        model = studentModel
        fields =['studentname','DEPARTMENT','email','contact','admissionnumber']
class  Student_ReportModelForm(ModelForm):
    class meta:
        model =Student_Report
        fields =['STUDENTID','cateogory','name','description','date','venue','certificate']            

class complaintModelForm(ModelForm):
    class meta:
        model =complaintModel
        fields = ['complaint','reply','date']

class notificationModelForm(ModelForm):
    class meta:
        model =notificationModel
        fields = ['date','notification']

class  resultModelForm(ModelForm):
    class meta:
        model =resultModel
        fields =['date','status','studentID','event']

class reportModelForm(ModelForm):
    class meta:
        model= reportModel 
        fields = ['status','event','file']                      


