from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import Department_form, EventModelForm, teacherModelForm
from .models import *

# Create your views here.

class Login(View):
    def get(self,request):
        return render(request,'administrator/loginpage.html')
    def post(self,request):
        username= request.POST['username']
        print(username)
        password= request.POST['password']
        login_obj= LoginModel.objects.get(username=username,password=password)
        print(login_obj)
        request.session["loginid"]=login_obj.id

        if login_obj.user_type =="admin":
            return HttpResponse(''' <script>alert("logged in successfully");window.location="/dashboard"</script>''')
        elif login_obj.Type  =="faculty":
            request.session['login_id']=login_obj.id
            return HttpResponse('''<script>alert("logged in successfully");window.location="/facultyhomepage"</script>''')    
class homepage(View):
    def get(self,request):
        return render(request,'administrator/homepage.html')
    
class eventregistration(View):
    def get(self,request):
        c= teacherModel.objects.all()
        return render(request,'administrator/eventregistration.html', {'teachers':c}) 
    def post(self,request):
        c=EventModelForm(request.POST,request.FILES)
        if c.is_valid():
            print(c)
            c.save()
            return HttpResponse('''<script>alert('event added successfully');window.location='/viewevent'</script>''')
    

class dashboard(View):
    def get(self,request):
        return render(request,'administrator/dashboard.html')
class manageevent(View):
    def get(self,request):
        return render(request,'administrator/manageevent.html')
    
class viewevent(View):
    def get(self,request):
        return render(request,'administrator/viewevent.html',)
class editevent(View):
    def get(self,request):
        return render(request,'administrator/editevent.html')
class deleteevent(View):
    def get(self,request,id):
        c=EventModel.objects.get(id=id)
        c.delete()
        return HttpResponse('''<script>alert('department deleted successfully');window.location='/viewevent'</script>''')
class editdepartment(View):
    def get(self,request,id):
        c=DepartmentModel.objects.get(id=id)
        return render(request,'administrator/editdepartment.html',{'data':c})
    def post(self,request,id):
        obj=DepartmentModel.objects.get(id=id)
        c=Department_form(request.POST,instance=obj)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert('department updated successfully');window.location='/viewdepartment'</script>''')
                    
class adddepartments(View):
    def get(self,request):
        return render(request,'administrator/adddepartment.html')
    def post(self,request):
        c=Department_form(request.POST)
        if c.is_valid():
            print(c)    
            c.save()
            return HttpResponse('''<script>alert('department added successfully');window.location='/viewdepartment'</script>''')

class delete(View):
    def get(self,request,id):
        c=DepartmentModel.objects.get(id=id)
        c.delete()
        return HttpResponse('''<script>alert('department deleted successfully');window.location='/viewdepartment'</script>''')
class editdepartment(View):
    def get(self,request,id):
        c=DepartmentModel.objects.get(id=id)
        return render(request,'administrator/editdepartment.html',{'data':c})
    def post(self,request,id):
        obj=DepartmentModel.objects.get(id=id)
        c=Department_form(request.POST,instance=obj)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert('department updated successfully');window.location='/viewdepartment'</script>''')
            
                      
          
class viewdepartment(View):
    def get(self,request):
        c = DepartmentModel.objects.all()
        return render(request,'administrator/viewdepartment.html', {'data':c})    
class eventreport(View):
    def get(self,request):
        return render(request,'administrator/eventreport.html') 
class complaint(View):
    def get(self,request):
        return render(request,'administrator/complaint.html')
class notification(View):
    def get(self,request):
        return render(request,'administrator/notification.html')
class varify(View):
    def get(self,request):
        return render(request,'administrator/varify.html')    
class participationresult(View):
    def get(self,request):
        return render(request,'administrator/participationresult.html')
class studeform(View):
    def get(self,request):
        return render(request,'administrator/studeform.html')
class teacherreg(View):
    def get(self,request):
        c = DepartmentModel.objects.all()
        return render(request,'administrator/teacherreg.html', {'data':c})
    def post(self,request):
        c=teacherModelForm(request.POST)
        print('#####################################################################', request.POST)
        if c.is_valid():
            reg = c.save(commit=False)
            teacher=LoginModel.objects.create(username=request.POST['username'],password=request.POST['password'],user_type='teacher')
            print('#####################################################################', teacher)
            reg.LOGIN_ID = teacher
            reg.save()
            return HttpResponse('''<script>alert('teacher added successfully');window.location='/viewteacher'</script>''')
class registrationview(View):
    def get(self,request):
        return render(request,"administrator/registrationview.html")
class faculty(View):
    def get(self,request):
        return render(request,'faculty/faculty.html') 
class complaint(View):
    def get(self,request):
        return render(request,'faculty/complaint.html')
class edit(View):
    def get(self,request):
        return render(request,'faculty/edit.html')
class publishjornal(View):
    def get(self,request):
        return render(request,'faculty/publishjornal.html') 
class rply(View):
    def get(self,request):
        return render(request,'faculty/rply.html')
class studentacheivement(View):
    def get(self,request):
        return render(request,'faculty/studentacheivement.html')
class studentrecord(View):
    def get(self,request):
        return render(request,'faculty/studentrecord.html')
class viewjournal(View):
    def get(self,request):
        return render(request,'faculty/viewjournal.html') 
class viewteacher(View):
    def get(self,request):
        return render(request,'faculty/viewteacher.html')                     
class home(View):
    def get(self,request):
        return render(request,'faculty/home.html')
class regestration(View):
    def get(self,request):
        return render(request,'faculty/regestration.html')
    def POST(self,request):
        form = teacherModelForm(request.POST)
        if form.is_valid():
            reg=form.save(commit=False)
            
            # reg.user = us
            reg.save()

            return HttpResponse('success')
        else:
            return HttpResponse('failed')
        
                          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            


