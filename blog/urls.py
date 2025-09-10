from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('' , blog_home_view , name= 'home'),
    path('<int:pid>' , blog_single_view , name= 'single'),
    path('category/<str:cat_name>' , blog_home_view , name= 'category'),
    path('author/<str:auth_name>' , blog_home_view , name= 'author'),
    path('search/' , blog_search , name= 'search'),
    path('test', test , name='test')
]

