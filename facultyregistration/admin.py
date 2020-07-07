from django.contrib import admin
from .models import DepartmentalCourses,DeptMembers,MembersChoice,SemesterCheck


admin.site.register(MembersChoice)
admin.site.register(DeptMembers)
admin.site.register(DepartmentalCourses)
admin.site.register(SemesterCheck)