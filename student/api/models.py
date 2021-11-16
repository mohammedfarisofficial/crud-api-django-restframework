from django.db import models

class Student(models.Model):
     name = models.CharField(max_length=200)
     branch = models.CharField(max_length=100)
     age = models.IntegerField()
     semester = models.IntegerField()
     cgpa = models.FloatField(null=True,blank=True)
     fee_paid = models.BooleanField(default=True)

     def __str__(self):
          return self.name
