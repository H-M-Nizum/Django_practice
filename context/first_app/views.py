from django.shortcuts import render

# Create your views here.


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# context syntax

def context_dic(request):
    dic = {'name': 'aaaaa', 'age': 23, 'language': ['python', 'c++', 'Mysql', 'Javascript'], 'courses': [
        
        {
            'id' : 1,
            'title': 'Python',
            'classes': 45
            
        },
        {
            'id' : 2,
            'title': 'Django',
            'classes': 50
            
        },
        {
            'id' : 3,
            'title': 'Mysql',
            'classes': 30
            
        },
        
    ]}
    return render(request, 'context_dic.html', dic)