from django import forms
from .models import Book

class UserForm(forms.Form):
    name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    subject = forms.CharField(max_length=60)
    email = forms.EmailField()


class InfoForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    addr = forms.CharField(max_length=40)
    phone = forms.IntegerField()


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=40)
    phone = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(max_length=30)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=30)

class FileForm(forms.Form):
    file_name = forms.CharField(max_length=40)
    file = forms.ImageField()


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Title', 'Author', 'Genre', 'Published_date', 'Image']

