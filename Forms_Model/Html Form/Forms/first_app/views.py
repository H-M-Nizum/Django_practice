from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        rating = request.POST.get('select')
        return render(request, 'about.html', {'name': name, 'email': email, 'Rating': rating})
    else:
        return render(request, 'about.html')

def form(request):
    # form a name set korbo
    return render(request, 'form.html')