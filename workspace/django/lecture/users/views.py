from django.shortcuts import render, redirect
from .forms import MemberForm, LoginForm
from .models import Member
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.http import HttpResponse
# Create your views here.


def login(request):
    login_form = LoginForm()
    return render(request, 'users/login.html', {'login_form': login_form})


def loginProcess(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        username = login_form.data['username']
        password = login_form.data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            django_login(request, user)
            return redirect('home')
        else:
            return HttpResponse('로그인 실패\n다시 로그인하세요')
    return redirect('home')


def logout(request):
    django_logout(request)
    return redirect('home')


def signup(request):
    member_form = MemberForm()
    return render(request, 'users/signup.html', {'member_form': member_form})


def signupProcess(request):
    if request.method == "POST":
        member_form = MemberForm(request.POST)
        if member_form.is_valid():
            if "image" in request.FILES.keys():
                new_user = Member.objects.create_user(
                    username=member_form.cleaned_data['username'],
                    email=member_form.cleaned_data['email'],
                    password=member_form.cleaned_data['password1'],
                    mobile=member_form.cleaned_data['mobile'],
                    image=request.FILES['image']
                )
            else:
                new_user = Member.objects.create_user(
                    username=member_form.cleaned_data['username'],
                    email=member_form.cleaned_data['email'],
                    password=member_form.cleaned_data['password1'],
                    mobile=member_form.cleaned_data['mobile'],
                )

            django_login(request, new_user)
            return redirect('home')
        else:
            return redirect('signup')
