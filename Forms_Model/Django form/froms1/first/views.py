from django.shortcuts import render
from . forms import contactform
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    # djform = contactform(request.POST)
    # djform contain fulll html form.. 
    # value gulu pawyar jonnne cleaned_data use korte hobe.
    # filaly form jodi valid hoy tahole amra cleaned_data pabo.
    # value gulu contain korar jonne request.POST use kortei hobe
    # if djform.is_valid():
    #     data = djform.cleaned_data
        
    #     return render(request, 'about.html', data)
        
    return render(request, 'about.html')


def form(request):
    if request.method == 'POST':
        djform = contactform(request.POST, request.FILES)
        if djform.is_valid():
            # # For file or img save
            # # chunk use for upload fister. file ar smaller version
            # file = djform.cleaned_data['File']
            # with open('./first/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            
            # # save thing for a image       
            # img = djform.cleaned_data['image']
            # with open('./first/upload/' + img.name, 'wb+') as destination:
            #     for chunk in img.chunks():
            #         destination.write(chunk)
                    
            data = djform.cleaned_data
            print(data)
            
    else:
        djform = contactform()
    return render(request, 'Dj_form.html', {'form': djform})


