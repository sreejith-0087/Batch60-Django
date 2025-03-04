from django.urls import path
from .views import *



urlpatterns = [
    path('wishes/', Wishes, name='wishes'),
    path('wishes2/', Wishes2, name='wishes2'),
    path('std_name/<str:nme>', Std_Name, name='std_name'),
    path('std_age/<int:age>', Std_Age, name='std_age'),
    path('', Base_Html, name='base_html'),
]
