from django.db import models


class AllocationList(models.Model):
    FacName = models.CharField(max_length=50)
    SubjectName = models.CharField(max_length=50)