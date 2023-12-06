from django.shortcuts import render
from posts.models import Post

# Create your views here.

def home(request):
    data = Post.objects.all()
    print(data)
    return render(request, 'home.html', {'data': data})