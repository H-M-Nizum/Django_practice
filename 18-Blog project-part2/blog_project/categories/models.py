from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    
    # database a name show korar jonne
    def __str__(self):
        return self.name