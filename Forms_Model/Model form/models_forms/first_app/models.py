from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.TextField()
    father_nmae = models.CharField(max_length=20, default='father')
    
    def __str__(self):
        return f"Roll - {self.roll} > Name - {self.name}"
    
    
# create models here for model forms
class studentmodel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.TextField()
    father_nmae = models.CharField(max_length=20, default='father')
    
    def __str__(self):
        return f"Roll - {self.roll} > Name - {self.name}"
    