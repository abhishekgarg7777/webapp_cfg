from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('demo/',views.demo, name='demo'),
    path('forms/', views.formsList, name="forms"),
    path('forms/<int:id>', views.questionList, name= "temp")
]