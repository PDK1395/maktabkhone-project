
from django.urls import path
from website.views import home_view , about_view , contact_view , blog_view , blog_home_view , blog_single_view

app_name = 'website'

urlpatterns = [

    path('', home_view , name= 'index'),
    path('about', about_view , name= 'about'),
    path('contact', contact_view , name= 'contact'),
    path('blog' , blog_view , name= 'blog'),
    path('blog-home' , blog_home_view , name= 'blog-home'),
    path('blog-single' , blog_single_view , name= 'blog-single'),
]