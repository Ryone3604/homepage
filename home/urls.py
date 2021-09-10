from django.urls import path
from . import views
from home.views import IndexView



urlpatterns = [
    path('', views.index, name='index'),
    path('works/', views.works, name='works'),
    path('works/<int:num>', views.works, name='works'),
    path('works/<str:url>', views.works_detail, name='works_detail'),
    path('about/', views.about, name='about'),
    
    path('contact/', views.IndexView.as_view(), name='contact'),
    path('blog/<int:num>', views.blog, name='blog'),
    path('blog/', views.blog, name='blog'),
    path('blog/<str:url>', views.blog_detail, name='blog_detail'),



    path('send/', views.IndexView.as_view(), name='send'),
    
    
    
]