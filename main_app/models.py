from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Type(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    role = models.CharField(max_length=100)


class Project(models.Model):
    user_link = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    

#f1
class F1(models.Model):
    name = models.CharField(max_length=100)
    bags = models.IntegerField(blank=True)
    location = models.CharField(max_length=100)
    vehicle = models.IntegerField(blank=True)
    trips = models.IntegerField(blank=True)
    time = models.CharField(max_length=100)

#f2
class F2(models.Model):
    name = models.CharField(max_length=100)
    garbage = models.CharField(max_length=100)
    bio = models.BooleanField()
    hazard = models.BooleanField()
    recycle = models.BooleanField()

class Form(models.Model):
    name = models.CharField(max_length=100)
    project_link = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="projects", null=True, blank=True)


class Question(models.Model):
    name = models.CharField(max_length=100)
    form_link = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='question', null=True, blank=True)


class Option(models.Model):
    name = models.CharField(max_length=100)
    question_link = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='option', null=True, blank=True)


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    # form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question_link = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question")
    answer = models.CharField(max_length=200)
