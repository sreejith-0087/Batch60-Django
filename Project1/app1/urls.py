from django.urls import path
from .views import *



urlpatterns = [
    path('wishes/', Wishes, name='wishes'),
    path('wishes2/', Wishes2, name='wishes2'),
    path('std_name/<str:nme>', Std_Name, name='std_name'),
    path('std_age/<int:age>', Std_Age, name='std_age'),
    path('base_html/', Base_Html, name='base_html'),
    path('static_file/', Static_File, name='static_file'),
    path('home/', Page_Redirection_Home, name='home'),
    path('about/', Page_Redirection_About, name='about'),
    path('contact/', Page_Redirection_Contact, name='contact'),
    path('template_home/', Template_Extending_Home, name='template_home'),
    path('template_about/', Template_Extending_About, name='template_about'),
    path('template_contact/', Template_Extending_Contact, name='template_contact'),
    path('datatohtml/', DataToHtml, name='datatohtml'),
    path('datatodb/', UserDetails, name='datatodb'),
    path('info/', Info, name='info'),
    path('profilecard/', ProfileCard, name='profilecard'),
    path('register/', Register, name='register'),
    path('login/', Login, name='login'),
    path('', Auth_Base, name='auth_base'),
    path('auth_reg/', Auth_Register, name='auth_reg'),
    path('auth_login/', Auth_Login, name='auth_login'),
    path('auth_logout/', Auth_Logout, name='auth_logout'),


]

