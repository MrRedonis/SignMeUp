from django.contrib import admin
from .models import Profile, Student, DeanOffice

# Register your models here.
admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(DeanOffice)
