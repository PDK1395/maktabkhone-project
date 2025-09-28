from django.urls import path
from . import views
#from accounts.views import *
app_name = 'accounts'

urlpatterns = [
    #login
    path('login' , views.login_view , name='login'),
    #logout
    path('logout' , views.logout_view , name= 'logout'),
    #register / signup
    path('signup/', views.signup_view, name='signup'), 
       
]
