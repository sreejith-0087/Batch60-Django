from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages, auth
from .models import *
from .forms import *
# Create your views here.


def Wishes(request):
    return HttpResponse('Good Morning!')

def Wishes2(request):
    return HttpResponse('Good Afternoon!')

def Std_Name(request, nme):
    return HttpResponse(f'Student Name: {nme}')

def Std_Age(request, age):
    return HttpResponse(f'Student Age: {age}')

def Base_Html(request):
    return render(request, '1.Base_Page.html')

def Static_File(request):
    return render(request, '2.Static_File.html')

def Page_Redirection_Home(request):
    return render(request, '3.Page_Redirection(Home).html')

def Page_Redirection_About(request):
    return render(request, '4.Page_Redirection(About).html')

def Page_Redirection_Contact(request):
    return render(request, '5.Page_Redirection(Contact).html')

def Template_Extending_Home(request):
    return render(request, '7.Template_Extending(Home).html')

def Template_Extending_About(request):
    return render(request, '8.Template_Extending(About).html')

def Template_Extending_Contact(request):
    return render(request, '9.Template_Extending(Contact).html')

def DataToHtml(request):
    data = Student_Details.objects.all()
    return render(request, '10.DatatoHtml.html', {'Details':data})


def UserDetails(request):
    if request.method == 'POST':
        a = UserForm(request.POST)

        if a.is_valid():
            nm = a.cleaned_data['name']
            ag = a.cleaned_data['age']
            sub = a.cleaned_data['subject']
            em = a.cleaned_data['email']

            b = UserModel(Name=nm, Age=ag, Subject=sub, Email=em)
            b.save()

            return HttpResponse('Success')
        else:
            return HttpResponse('Failed')

    return render(request, '11.Forms.html')


def Info(request):
    if request.method == 'POST':
        user = InfoForm(request.POST)

        if user.is_valid():
            nm = user.cleaned_data['name']
            ad = user.cleaned_data['addr']
            em = user.cleaned_data['email']
            ph = user.cleaned_data['phone']

            b = InfoModel(Name=nm, Email=em, Address=ad, Phone=ph)
            b.save()

            return redirect('/')
        else:
            return HttpResponse('Failed')

    return render(request, '12.Info.html')


def ProfileCard(request):
    data = InfoModel.objects.all()
    return render(request, '13.Profile_Card.html', {'profile': data})


def Register(request):
    if request.method == 'POST':
        regform = RegisterForm(request.POST)

        if regform.is_valid():
            nm = regform.cleaned_data['name']
            ph = regform.cleaned_data['phone']
            em = regform.cleaned_data['email']
            pwd = regform.cleaned_data['password']

            b = RegisterModel(Name=nm, Phone=ph, Email=em, Password=pwd)
            b.save()

            return redirect('/login')
        else:
            return HttpResponse('Registration Failed')
    return render(request, '14.Register.html')


def Login(request):
    if request.method == 'POST':
        logform = LoginForm(request.POST)

        if logform.is_valid():
            em = logform.cleaned_data['email']
            pwd = logform.cleaned_data['password']

            b = RegisterModel.objects.all()

            for i in b:
                if em == i.Email and pwd == i.Password:
                    return HttpResponse('Login Success')
            else:
                return HttpResponse('Login Failed')
        else:
            return HttpResponse('Invalid Login')
    return render(request, '15.Login.html')


def Auth_Base(request):
    return render(request, '16.Auth_Base.html')

def Auth_Register(request):
    if request.method == 'POST':
        nm = request.POST['Name']
        em = request.POST['Email']
        pwd = request.POST['Password']
        re_pwd = request.POST['Re-Password']

        if pwd == re_pwd:
            if User.objects.filter(email=em).exists():
                messages.error(request, 'Email Already Exist!')
            else:
                user = User.objects.create_user(username=em, first_name=nm, email=em, password=pwd)
                user.save()
                messages.success(request, 'Registration Completed')
                return redirect('/auth_login')
        else:
            messages.error(request, 'Password does not match')
    return render(request, '17.Auth_Register.html')


def Auth_Login(request):
    if request.method == 'POST':
        email = request.POST['Email']
        password = request.POST['Password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Complete')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Login')
    return render(request, '18.Auth_Login.html')


def Auth_Logout(request):
    logout(request)
    return redirect('/')


