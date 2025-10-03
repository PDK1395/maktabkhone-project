from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import re

# تابع برای بررسی ایمیل
def is_valid_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return re.match(regex, email) is not None

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username_email = request.POST['username_email']  # ورودی نام کاربری یا ایمیل
            password = request.POST['password']
            
            # بررسی اینکه ورودی ایمیل هست یا نام کاربری
            if is_valid_email(username_email):
                # جستجو برای ایمیل
                try:
                    user = User.objects.get(email=username_email)  # پیدا کردن کاربر با ایمیل
                    user = authenticate(request, username=user.username, password=password)  # احراز هویت با نام کاربری
                except User.DoesNotExist:
                    user = None
            else:
                # جستجو برای نام کاربری
                user = authenticate(request, username=username_email, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                # اگر اعتبارسنجی نام کاربری و رمز عبور اشتباه باشد
                form = AuthenticationForm()
                context = {'form': form, 'error': 'نام کاربری یا رمز عبور اشتباه است.'}
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
            form = UserCreationForm(request.POST)
            if form.is_valid():
                # بررسی اینکه ایمیل تکراری نباشد
                email = form.cleaned_data.get('email')
                username = form.cleaned_data.get('username')

                # اگر ایمیل تکراری باشد، خطا را نشان بده
                if User.objects.filter(email=email).exists():
                    form.add_error('email', 'این ایمیل قبلاً استفاده شده است.')
                    context = {'form': form}
                    return render(request, 'accounts/signup.html', context)
                
                # در غیر این صورت، ثبت‌نام را انجام بده
                form.save()
                return redirect('accounts:login')
        else:
            form = UserCreationForm()

        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')
