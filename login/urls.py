
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginmodule/',include('loginmodule.urls')),
    path('facultyregistration/',include('facultyregistration.urls')),
    path('CourseAllocation/',include('CourseAllocation.urls')),
]
