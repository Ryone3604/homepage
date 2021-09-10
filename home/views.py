from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Movie
from django.core.paginator import Paginator
from django.views import generic
from . import forms
from django.urls import reverse_lazy

def index(request, num=1):
    date = Movie.objects.all().order_by('published_date').reverse()
    date2 = Post.objects.all().order_by('published_date').reverse()
    page = Paginator(date, 5)
    page2 = Paginator(date2, 1)
    params ={
        'title':'Top',
        'msg':'toppagedesu.',
        'date':page.get_page(num),
        'date2':page2.get_page(num)
        
    }
    return render(request, 'home/top.html', params)

def works(request, num=1):
    date = Movie.objects.all().order_by('published_date').reverse()
    page = Paginator(date, 3)
    params ={
        'title':'Music',
        'msg':'workpagedesu.',
        'date':page.get_page(num)
    }
    return render(request, 'home/works.html', params)

def works_detail(request, url):
    date = Movie.objects.filter(url=url)
    params ={
        'title':'Music',
        'msg':'workpagedesu.',
        'date':date
    }
    return render(request, 'home/works_detail.html', params)

    


def about(request):
    params ={
        'title':'About',
        'msg':'aboutpagedesu.',
    }
    return render(request, 'home/index.html', params)

def blog(request, num=1):
    date = Post.objects.all().order_by('published_date').reverse()
    page = Paginator(date, 3)
    params ={
        'title':'Blog',
        'msg':'blogpagedesu.',
        'date':page.get_page(num)
    }
    return render(request, 'home/blog.html', params)

def blog_detail(request, url):
    date = Post.objects.filter(url=url)
    params ={
        'title':'Blog',
        'msg':'blogpagedesu.',
        'date':date
    }
    return render(request, 'home/blog_detail.html', params)



class IndexView(generic.FormView):
    template_name = "home/contact.html"
    form_class = forms.InquiryForm
    success_url = "http://127.0.0.1:8000/home/"
    

    def form_valid(self,form):
        form.send_email()
        return super().form_valid(form)    
    

def contact(request):
    params ={
        'title':'contact',
        'msg':'cantactpagedesu.',
    }
    
    return render(request, 'home/contact.html', params)
    
    
        

    
#def send(request):
 #   params ={
  #      'title':'top',
   ##}
    
    #if request.method == 'POST':
        
     #   form = forms.InquiryForm(request.POST)
        

#        if form.is_valid():
            
 #           message = form.cleaned_data['message']
  #          email = form.cleaned_data['sender']
   #         recipients = [settings.EMAIL_HOST_USER]
            
    #        try:
     #           send_mail(message, email, recipients)
      #      except BadHeaderError:
       #         return HttpResponse('無効なヘッダーが見つかりました。')
        #    return redirect('home/index.html',params)
    #else:
     #   form = InquiryForm()




    #return render(request, 'home/context.html', params)
    




    


# Create your views here.
