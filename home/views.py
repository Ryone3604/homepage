from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator

def index(request):
    params ={
        'title':'top',
        'msg':'toppagedesu.',
    }
    return render(request, 'home/index.html', params)

def works(request):
    params ={
        'title':'works',
        'msg':'workpagedesu.',
    }
    return render(request, 'home/works.html', params)

def about(request):
    params ={
        'title':'about',
        'msg':'aboutpagedesu.',
    }
    return render(request, 'home/index.html', params)

def blog(request, num=1):
    date = Post.objects.all().order_by('published_date').reverse()
    page = Paginator(date, 3)
    params ={
        'title':'blog',
        'msg':'blogpagedesu.',
        'date':page.get_page(num)
    }
    return render(request, 'home/blog.html', params)

def contact(request):
    params ={
        'title':'contact',
        'msg':'cantactpagedesu.',
    }
    return render(request, 'home/index.html', params)
# Create your views here.
