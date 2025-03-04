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
