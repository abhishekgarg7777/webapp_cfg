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
    def __str__(self):
        return self.name


class Form(models.Model):
    name = models.CharField(max_length=100)
    project_link = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="projects", null=True, blank=True)
    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=100)
    form_link = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='question', null=True, blank=True)
    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(max_length=100)
    question_link = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='option', null=True, blank=True)
    def __str__(self):
        return self.name


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    # form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question_link = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question")
    answer = models.CharField(max_length=200)