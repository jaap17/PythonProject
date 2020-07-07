from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib import admin, auth, messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from facultyregistration.models import DeptMembers, SemesterCheck


def index(request):
    return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        loginuname = request.POST['username']
        loginpass = request.POST['password']
        if loginuname == 'F001' and loginpass == 'F0012000':
            request.session['hod'] = loginuname
            name = 'Dr H P Singh'
            return HttpResponseRedirect('/loginmodule/hodhomepage/')
        else:
            #user = auth.authenticate(username=loginuname,password=loginpass)

            #if user is not None:
                #auth.login(request, user)
            Faculty = DeptMembers.objects.filter(FacId=loginuname)
            if not Faculty or loginpass == loginuname:
                return HttpResponseRedirect('/loginmodule/invalidlogin/')
            else:
                sem = SemesterCheck.objects.all()
                recordnum = SemesterCheck.objects.count()
                if recordnum == 0:
                    message = "The forms of the Choice Filling are not Generated"
                    return render(request, 'formnotgenerated.html', {'message': message, 'user': Faculty})
                return render(request, 'loggedin.html', {'user': Faculty, 'uname': loginuname, 'sem': sem})




def loggedin(request):
    # faculty = request.session['faculty']
    sem = SemesterCheck.objects.all()
    recordnum = SemesterCheck.objects.all().aggregate(Count('path'))
    if recordnum == 0:
        return render(request, 'formnotgenerated.html')
    elif recordnum == 1:
        message = "Semester Selected"
        return render(request, 'loggedin.html')


@login_required(login_url='/loginmodule/index/')
def logout(request):
    return render(request, 'logout.html')


@login_required(login_url='/loginmodule/index/')
def invalidlogin(request):
    return render(request, 'invalidlogin.html')


@login_required(login_url='/loginmodule/index/')
def hodhomepage(request):
    hodname = 'Dr H P Singh'
    return render(request, 'hodhomepage.html',{'hodname':hodname})
