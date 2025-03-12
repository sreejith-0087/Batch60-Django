from django import forms


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

