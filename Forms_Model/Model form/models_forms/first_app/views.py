from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    # every student record is a object.
    # object.all() return all object in a list
    student = models.Student.objects.all()
    # for i in student:
    #     print(i.name, i.roll, i.address, i.father_nmae)
    # print(student)
    return render(request, 'home.html', {'student': student})

