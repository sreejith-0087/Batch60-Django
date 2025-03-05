from django.urls import path
from .views import *



urlpatterns = [
    path('wishes/', Wishes, name='wishes'),
    path('wishes2/', Wishes2, name='wishes2'),
    path('std_name/<str:nme>', Std_Name, name='std_name'),
    path('std_age/<int:age>', Std_Age, name='std_age'),
    path('base_html/', Base_Html, name='base_html'),
    path('static_file/', Static_File, name='static_file'),
    path('', Page_Redirection_Home, name='home'),
    path('about/', Page_Redirection_About, name='about'),
    path('contact/', Page_Redirection_Contact, name='contact'),
]



