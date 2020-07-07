from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('facultyselect/', views.facultyselect, name='facultyselect'),
    path('courseselect/',views.courseselect,name='courseselect'),
    path('CourseAllocation/',views.courseallocation,name='CourseAllocation'),
    path('hodhomepage/',views.index,name='index'),
    path('callfacultyadd/',views.callfacultyadd,name='callfacultyadd'),
    path('facultyadd/',views.facultyadd,name='facultyadd'),
    path('callfacultydelete/',views.callfacultydelete,name='callfacultydelete'),
    path('facultydelete/',views.facultydelete,name='facultydelete'),
    path('evencall/',views.evencall,name='evencall'),
    path('addcourse/',views.addcourse,name='addcourse'),
    path('calladdcourse/',views.calladdcourse,name='calladdcourse'),
    path('removecourse/',views.removecourse,name='removecourse'),
    path('callremovecourse/',views.callremovecourse,name='callremovecourse'),
    path('oddcall/',views.oddcall,name='oddcall'),
    path('callchoicefillingform/',views.callchoicefillingform,name='callchoicefillingform'),
    path('generateform/',views.generateform,name='generateform'),
    path('calloddchoicefillingform/',views.calloddchoicefillingform,name='calloddchoicefillingform'),
    path('Storeoddchoices/',views.Storeoddchoices,name='Storeoddchoices'),
    path('generateformdecider/',views.generateformdecider,name='generateformdecider'),
    path('evenform/',views.evenform,name='evenform'),
    path('oddform/',views.oddform,name='oddform'),
    #path('courseset/',views.courseset,name='courseset'),
    #path('callcheck/',views.callcheck,name='callcheck'),
]
