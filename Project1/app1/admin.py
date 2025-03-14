from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Student_Details)

admin.site.register(UserModel)

class InfoAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Address', 'Phone']
    list_editable = ['Email', 'Phone']
    search_fields = ['Name', 'Email', 'Phone']
admin.site.register(InfoModel, InfoAdmin)


@admin.register(RegisterModel)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Phone', 'Email']
    list_editable = ['Phone', 'Email']


admin.site.register(FileModel)

admin.site.register(Author)

admin.site.register(Genre)

admin.site.register(Book)