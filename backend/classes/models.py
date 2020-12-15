from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Subject(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Classes(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    is_lecture = models.BooleanField(default=False)
    is_auditorium = models.BooleanField(default=False)
    is_laboratory = models.BooleanField(default=False)
    is_project = models.BooleanField(default=False)
    day_of_week = models.IntegerField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    max_students = 0

    def __str__(self):
        return self.subject.name

    def set_max_students(self, is_auditorium, is_laboratory, is_project):
        if is_auditorium:
            self.max_students = 30
        elif is_laboratory:
            self.max_students = 15
        elif is_project:
            self.max_students = 15
        else:
            self.max_students = 300
