from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from classes.models import Subject


class Account(User):
    is_student = models.BooleanField(default=False)
    is_dean_office = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    field_of_study = models.CharField(max_length=100, blank=True)
    teacher = models.ManyToManyField(Subject)

    def __str__(self):
        return f'{self.user.username} Profile'


class DeanOffice(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
