from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import re
from accounts.forms import CustomUserCreationForm


def is_valid_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return re.match(regex, email) is not None

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username_email = request.POST['username_email']  
            password = request.POST['password']
            

            if is_valid_email(username_email):

                try:
                    user = User.objects.get(email=username_email) 
                    user = authenticate(request, username=user.username, password=password) 
                except User.DoesNotExist:
                    user = None
            else:

                user = authenticate(request, username=username_email, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:

                form = AuthenticationForm()
                context = {'form': form, 'error': 'username or password is wrong .'}
                return render(request, 'accounts/login.html', context)
        else:
            form = AuthenticationForm()
            context = {'form': form}
            return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')


@login_required
def logout_view(request):
    logout(request )
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():

                email = form.cleaned_data.get('email')
                username = form.cleaned_data.get('username')


                if User.objects.filter(email=email).exists():
                    form.add_error('email', 'this email has been used befor .')
                    context = {'form': form}
                    return render(request, 'accounts/signup.html', context)
                

                form.save()
                return redirect('accounts:login')
        else:
            form = CustomUserCreationForm()

        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')
