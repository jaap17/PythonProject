from django.http import response, HttpResponse
from django.shortcuts import render
from .models import DepartmentalCourses, DeptMembers, MembersChoice, SemesterCheck


def facultyselect(request):
    faculties = DeptMembers.objects.all()
    return render(request, 'facultyregister.html', {'faculties': faculties})


def index(request):
    return render(request, 'hodhomepage.html')


def courseselect(request):
    Courses = DepartmentalCourses.objects.all()
    return render(request, 'courseregister.html', {'Courses': Courses})


def courseallocation(request):
    return render(request, 'CourseAllocation.html')


def callfacultyadd(request):
    return render(request, 'facultyadd.html')


def callfacultydelete(request):
    return render(request, 'facultydelete.html')


def facultydelete(request):
    FacultyId = request.POST['facid']
    if DeptMembers.objects.filter(FacId=FacultyId).exists():
        DeptMembers.objects.filter(FacId=FacultyId).delete()
        message = "Data deleted succesfully"
    else:
        message = "This Faculty does not exist so deletion not possible"
    return render(request, 'facultydeletesuccess.html', {'message': message})


def facultyadd(request):
    FacultyId = request.POST['facid']
    FacultyName = request.POST['facname']
    if DeptMembers.objects.filter(FacId=FacultyId).exists():
        message = "Insertion not possible as the Faculty already exists"
    else:
        c = DeptMembers(FacId=FacultyId, FacName=FacultyName)
        c.save()
        message = "New data inserted succesfully"
    return render(request, 'facultyaddsuccess.html', {'message': message})


def evencall(request):
    Sem2 = DepartmentalCourses.objects.filter(Semester=2)
    Sem4 = DepartmentalCourses.objects.filter(Semester=4)
    Sem6 = DepartmentalCourses.objects.filter(Semester=6)
    return render(request, 'evencourses.html', {'Sem2': Sem2, 'Sem4': Sem4, 'Sem6': Sem6})


def oddcall(request):
    Sem3 = DepartmentalCourses.objects.filter(Semester=3)
    Sem5 = DepartmentalCourses.objects.filter(Semester=5)
    Sem7 = DepartmentalCourses.objects.filter(Semester=7)
    return render(request, 'oddcourses.html', {'Sem3': Sem3, 'Sem5': Sem5, 'Sem7': Sem7})


def calladdcourse(request):
    return render(request, 'addcourse.html')


def addcourse(request):
    cid = request.POST['courseid']
    cname = request.POST['coursename']
    sem = request.POST['semester']
    if DepartmentalCourses.objects.filter(CourseId=cid).exists():
        message = "The course already exists so can't be added again"
    else:
        c = DepartmentalCourses(CourseId=cid, CourseName=cname, Semester=sem)
        c.save()
        message = "Course Addition succesful"
    return render(request, 'addcoursesuccess.html', {'message': message})


def callremovecourse(request):
    return render(request, 'removecourse.html')


def removecourse(request):
    cid = request.POST['courseid']
    if DepartmentalCourses.objects.filter(CourseId=cid).exists():
        DepartmentalCourses.objects.filter(CourseId=cid).delete()
        message = "Course Deleted Succesfully"
    else:
        message = "Course cannot be Deleted as it does not Exist"
    return render(request, 'removecoursesuccess.html', {'message': message})


def callchoicefillingform(request):
    name = request.GET['facultyname']
    path1 = request.GET['path']
    Semx = DepartmentalCourses.objects.filter(Semester=2)
    Semy = DepartmentalCourses.objects.filter(Semester=4)
    Semz = DepartmentalCourses.objects.filter(Semester=6)
    return render(request, 'choicefilling.html', {'Semx': Semx, 'Semy': Semy, 'Semz': Semz, 'name': name, 'path': path1})


def generateform(request):
    return render(request, 'Formtypeselection.html')


def generateformdecider(request):
    sem = request.POST['sem']
    if sem == 'ODD':
        message = "ODD Semester Selected"
        sempath = '/facultyregistration/calloddchoicefillingform/'
        sempath1 = '/facultyregistration/oddform/'
        c = SemesterCheck(path=sempath)
        # c.save()

    elif sem == 'EVEN':
        message = "EVEN Semester Selected"
        sempath = '/facultyregistration/callchoicefillingform/'
        sempath1 = '/facultyregistration/evenform/'
        c = SemesterCheck(path=sempath)
        # c.save()

    return render(request, 'gotochoicefillingform.html', {'path': sempath, 'message': message, 'sempath1': sempath1})


def calloddchoicefillingform(request):
    name = request.GET['facultyname']
    path1 = request.GET['path']
    Semx = DepartmentalCourses.objects.filter(Semester=3)
    Semy = DepartmentalCourses.objects.filter(Semester=5)
    Semz = DepartmentalCourses.objects.filter(Semester=7)
    return render(request, 'choicefilling.html', {'Semx': Semx, 'Semy': Semy, 'Semz': Semz, 'name': name, 'path': path1})


def Storeoddchoices(request):
    list = []
    list1 = []
    facname = request.GET['facultyname']
    path = request.GET['path']
    priority1 = request.GET['priority1']
    choice = DepartmentalCourses.objects.get(CourseId=priority1)
    first = choice.CourseName
    list.append(choice)
    list1.append("priority1")
    priority2 = request.GET['priority2']
    choice1 = DepartmentalCourses.objects.get(CourseId=priority2)
    second = choice1.CourseName
    list.append(choice1)
    list1.append("priority2")
    priority3 = request.GET['priority3']
    choice2 = DepartmentalCourses.objects.get(CourseId=priority3)
    third = choice2.CourseName
    list.append(choice2)
    list1.append("priority3")
    priority4 = request.GET['priority4']
    choice3 = DepartmentalCourses.objects.get(CourseId=priority4)
    fourth = choice3.CourseName
    list.append(choice3)
    list1.append("priority4")
    priority5 = request.GET['priority5']
    choice4 = DepartmentalCourses.objects.get(CourseId=priority5)
    fifth = choice4.CourseName
    list.append(choice4)
    list1.append("priority5")
    if priority1 != priority2 != priority3 != priority4 != priority5:
        if MembersChoice.objects.filter(FacName=facname).exists():
            MembersChoice.objects.filter(FacName=facname).delete()
            c = MembersChoice(FacName=facname, priority1=first, priority2=second, priority3=third,
             priority4=fourth, priority5=fifth)
            c.save()
        else:
            c = MembersChoice(FacName=facname, priority1=first, priority2=second, priority3=third,
            priority4=fourth, priority5=fifth)
            c.save()
        return render(request, 'display.html', {'priority': list, 'facname': facname})
    else:
        return render(request, 'ErrorChoice.html', {'path': path,'facname':facname})


def evenform(request):
    Semx = DepartmentalCourses.objects.filter(Semester=2)
    Semy = DepartmentalCourses.objects.filter(Semester=4)
    Semz = DepartmentalCourses.objects.filter(Semester=6)
    return render(request, 'choicefilling.html', {'Semx': Semx, 'Semy': Semy, 'Semz': Semz})


def oddform(request):
    Semx = DepartmentalCourses.objects.filter(Semester=3)
    Semy = DepartmentalCourses.objects.filter(Semester=5)
    Semz = DepartmentalCourses.objects.filter(Semester=7)
    return render(request, 'choicefilling.html', {'Semx': Semx, 'Semy': Semy, 'Semz': Semz})
