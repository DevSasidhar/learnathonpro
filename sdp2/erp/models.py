from django.db import models

# Create your models here.

DEPARTMENT_CHOICES = [
    ("CSE",'cse'),
    ("CSIT",'csit'),
    ("AIDS",'aids'),
]

class Student(models.Model):
    regid=models.IntegerField()
    name=models.CharField(max_length=100)
    dept=models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    def __str__(self):
        return self.name