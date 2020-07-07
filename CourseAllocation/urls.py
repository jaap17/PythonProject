from django.urls import path
from . import views

urlpatterns = [
    path('Allocation/', views.getcourseallocation, name='getCourseAllocation'),
    path('storeallocation/',views.storeallocation,name='storeallocation'),
    path('courseallocation/',views.courseallocation,name='courseallocation'),
    path('viewallocation/',views.viewallocation,name='viewallocation'),
    path('facultyallocation/',views.facultyallocation,name='facultyallocation'),
]
