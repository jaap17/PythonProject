from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('loggedin/', views.loggedin, name='loggedin'),
    path('invalidlogin/',views.invalidlogin,name='invalidlogin'),
    path('hodhomepage/',views.hodhomepage,name='hodhomepage'),

]
