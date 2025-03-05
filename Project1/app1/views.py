from django.shortcuts import render
from django.http import HttpResponse
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

