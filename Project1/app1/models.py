from django.db import models

# Create your models here.

class Student_Details(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Subject = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class UserModel(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Subject = models.CharField(max_length=60)
    Email = models.EmailField()
    def __str__(self):
        return self.Name

class InfoModel(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Address = models.CharField(max_length=40)
    Phone = models.IntegerField()

    def __str__(self):
        return self.Name


class RegisterModel(models.Model):
    Name = models.CharField(max_length=40)
    Phone = models.IntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=30)

    def __str__(self):
        return self.Name

