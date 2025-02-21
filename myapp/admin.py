from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(LoginModel)
admin.site.register(EventModel)
admin.site.register(DepartmentModel)
admin.site.register(teacherModel)
admin.site.register(studentModel)
admin.site.register(complaintModel)
admin.site.register(notificationModel)
admin.site.register(resultModel)
admin.site.register(reportModel)