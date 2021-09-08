from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('works/', views.works, name='works'),
    path('works/<int:num>', views.works, name='works'),
    path('about/', views.about, name='about'),
    
    path('contact/', views.contact, name='contact'),
    path('blog/<int:num>', views.blog, name='blog'),
    path('blog/', views.blog, name='blog'),
    
    
    
]