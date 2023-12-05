from django.shortcuts import render, redirect
from . import models
from first_app.forms import studentForm
# Create your views here.

def home(request):
    # every student record is a object.
    # object.all() return all object in a list
    student = models.Student.objects.all()
    # for i in student:
    #     print(i.name, i.roll, i.address, i.father_nmae)
    # print(student)
    return render(request, 'home.html', {'student': student})

# for delete a record in table
def delete_student(request, roll):
    #  pk means primary key
    std = models.Student.objects.get(pk = roll).delete()
    return redirect('home')


# for model form
def model_form(request):
    std = studentForm()
    return render(request, 'model_form.html', {'form': std}) 