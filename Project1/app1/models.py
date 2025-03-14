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


class FileModel(models.Model):
    File_Name = models.CharField(max_length=40)
    File = models.ImageField()

    def __str__(self):
        return self.File_Name

class Author(models.Model):
    Name = models.CharField(max_length=40)
    # Other fields
    def __str__(self):
        return self.Name

class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre


class Book(models.Model):
    Title = models.CharField(max_length=60)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Genre = models.ManyToManyField(Genre)
    Published_date = models.DateField()
    Image = models.ImageField(upload_to='Books/', null=True, blank=True)

    def __str__(self):
        return self.Title

