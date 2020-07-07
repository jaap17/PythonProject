from django.db.models import Count
from django.shortcuts import render
from facultyregistration.models import MembersChoice, DeptMembers, DepartmentalCourses,SemesterCheck
from .models import AllocationList


def getcourseallocation(request):
    sem2 = DepartmentalCourses.objects.filter(Semester=2)
    sem4 = DepartmentalCourses.objects.filter(Semester=4)
    sem6 = DepartmentalCourses.objects.filter(Semester=6)
    count1 = DeptMembers.objects.count()
    count1 = count1 - 1
    recordnum = MembersChoice.objects.all().count()
    if recordnum == count1:
        message = "All the faculties have given their choice"
        choicerecords = MembersChoice.objects.all()
        return render(request, 'Allocation.html',
                      {'record': recordnum, 'choice': choicerecords, 'sem2': sem2, 'sem4': sem4, 'sem6': sem6,
                       'message': message})
    else:
        message = "All the faculties have not given their choices"
        return render(request,'errorallocation.html',{'message':message})


def courseallocation(request):
    list = []
    sem2 = DepartmentalCourses.objects.filter(Semester=2)
    sem4 = DepartmentalCourses.objects.filter(Semester=4)
    sem6 = DepartmentalCourses.objects.filter(Semester=6)

    return render(request, 'CourseAllocation.html', {'sem2': sem2, 'sem4': sem4, 'sem6': sem6})


def storeallocation(request):
    list = []
    Pankaj = request.POST['Dr Pankaj Jalote']
    list.append(Pankaj)
    Meena = request.POST['Meena Mathur']
    list.append(Meena)
    Amit = request.POST['Amit Patel']
    list.append(Amit)
    Khushali = request.POST['Khushali Pandya']
    list.append(Khushali)
    Vrajesh = request.POST['Vrajesh Sharma']
    list.append(Vrajesh)
    Rajesh = request.POST['Rajesh Patel']
    list.append(Rajesh)
    Jay = request.POST['Jay Shah']
    list.append(Jay)
    Ajay = request.POST['Ajay Thakur']
    list.append(Ajay)
    Ramesh = request.POST['Ramesh Varma']
    list.append(Ramesh)
    JayPatel = request.POST['Jay Patel']
    list.append(JayPatel)
    c = AllocationList(FacName='Dr Pankaj Jalote',SubjectName=Pankaj)

    c.save()

    c = AllocationList(FacName='Meena Mathur', SubjectName= Meena)
    c.save()
    c = AllocationList(FacName='Amit Patel', SubjectName= Amit)
    c.save()
    c = AllocationList(FacName='Khushali Pandya', SubjectName= Khushali)
    c.save()
    c = AllocationList(FacName='Vrajesh Sharma', SubjectName=Vrajesh)
    c.save()
    c = AllocationList(FacName='Rajesh Patel', SubjectName= Rajesh)
    c.save()
    c = AllocationList(FacName='Ajay Thakur', SubjectName= Ajay)
    c.save()
    c = AllocationList(FacName='Ramesh Varma', SubjectName=Ramesh)
    c.save()
    c = AllocationList(FacName='Jay Shah', SubjectName=Jay)
    c.save()
    c = AllocationList(FacName='Jay Patel',SubjectName=JayPatel)
    c.save()
    list = AllocationList.objects.all()
    return render(request, 'showAllocation.html', {'list': list})


def viewallocation(request):
    name = request.GET['facname']
    obj = AllocationList.objects.all()
    count = AllocationList.objects.count()
    if count == 0:
        message = "The allocation has not been done Yet"
        return render(request, 'allocationlist1.html', {'message': message})
    else:
        message = "The Allocation list is as under"
        return render(request,'allocationlist.html',{'message':message , 'object':obj,'name':name})


def facultyallocation(request):
    name = request.GET['name']
    obj = AllocationList.objects.all()
    count = AllocationList.objects.count()
    if count == 0:
        message = "The allocation has not been done Yet"
        return render(request, 'allocationlist1.html', {'message': message})
    else:
        message = "The Allocation list is as under"
        return render(request, 'Allocationlist2.html', {'message': message, 'object': obj, 'name': name})