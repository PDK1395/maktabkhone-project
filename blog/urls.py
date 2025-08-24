from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('home' , blog_home_view , name= 'home'),
    path('single' , blog_single_view , name= 'single'),
    path('post-<int:pid>' , test , name= 'test'),
]

