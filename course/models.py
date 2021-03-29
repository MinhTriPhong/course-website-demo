from django.db import models
import random as rd
# Create your models here.
class course(models.Model):
    course_id = models.DecimalField(max_digits=4,default=rd.randint(0,9999),decimal_places=0)
    Course_name=models.TextField()
    Lecture_name = models.TextField()
    Duration = models.DecimalField(default=11,max_digits=3,decimal_places=0)
