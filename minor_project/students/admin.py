from django.contrib import admin

# Register your models here.
from .models import Student,College
admin.site.register(Student)
admin.site.register(College)
