from django.db import models
from datetime import datetime    
import random
# Create your models here.
class student(models.Model):
    student_id = models.DecimalField(max_digits=6,default=random.randint(0,99999),decimal_places=0)
    name = models.TextField(blank=False)
    age = models.IntegerField(default="0",blank=False)
    date_of_birth = models.DateField(default=datetime.today(),blank = False)
    #course_attend = models.cho
    