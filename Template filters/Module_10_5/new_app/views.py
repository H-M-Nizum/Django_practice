from django.shortcuts import render

import datetime
# Create your views here.
def context(request):
    
   



    

    
    dic = {'name' : 'aaaa', 'age': 23, 'language': ['python', 'django', 'mysql', 'javascript'], 'value': 30, 'emptyvalue': '', 'string': 'Django is best python framework', 'birthday' : datetime.datetime.now(), 'd' : [
        {'name' : 'ta', 'age': 30},
        {'name' : 'ba', 'age': 13},
        {'name' : 'alif', 'age': 23},
        {'name' : 'cha', 'age': 3},
        
        
    ], 'line': 'Hello\nmy name is Django.\nI am a python framwoek.',    
           
    'mybirthdate': datetime.datetime(2004, 11, 18),   
    'mydate': datetime.datetime(2020, 5, 17), 
    
    
    'subject' : ['problem solving', ['c', 'c++', 'Algo', 'Datastructure'], 'SOftware', ['OOP', "Database", 'Django']]
    
    
    }
    
    return render(request, 'context.html', dic)