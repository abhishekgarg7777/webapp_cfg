from django.shortcuts import render
from main_app import models


# Create your views here.
def demo(request):
    return render(request, 'demo.html')


def formsList(request):
    project_list = models.Project.objects.all().filter(user_link=request.user)
    forms = []
    for i in project_list:
        forms.append(models.Form.objects.all().filter(project_link = i).get())
    return render(request, 'forms.html', context={'forms': forms, 'username': request.user.username})


