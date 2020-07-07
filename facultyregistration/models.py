from django.db import models


# Create your models here.


class DeptMembers(models.Model):
    FacId = models.CharField(max_length=5)
    FacName = models.CharField(max_length=40)


class DepartmentalCourses(models.Model):
    CourseId = models.CharField(max_length=5, primary_key=True)
    CourseName = models.CharField(max_length=50)
    Semester = models.IntegerField()


class MembersChoice(models.Model):
    FacName = models.CharField(max_length=50)
    priority1 = models.CharField(max_length=40)
    priority2 = models.CharField(max_length=40)
    priority3 = models.CharField(max_length=40)
    priority4 = models.CharField(max_length=40)
    priority5 = models.CharField(max_length=40)


class SemesterCheck(models.Model):
    path = models.CharField(max_length=50)