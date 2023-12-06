from django.db import models
from author.models import Author

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    
    # one to one relation ship.
    # akjon author ar aktai profile thakbe.
    author = models.OneToOneField(Author, on_delete=models.CASCADE, default=None)
    
    
    # database a name show korar jonne
    def __str__(self):
        return self.name