from django.shortcuts import render
from main_app import models


# Create your views here.
def demo(request):
    return render(request, 'demo.html')


def formsList(request):
    project_list = models.Project.objects.all().filter(user_link=request.user)
    forms = []
    for i in project_list:
        forms.append(models.Form.objects.all().filter(project_link=i).get())
    return render(request, 'forms.html', context={'forms': forms, 'username': request.user.username})


def questionList(request, id):
    ques_list = models.Question.objects.all().filter(form_link=id).order_by('id')
    print("Questions list")
    print(ques_list)
    ques = []
    ques_dict = {}
    for i in range(ques_list.count()):
        ques.append([ques_list.all()[i], models.Option.objects.all().filter(question_link=ques_list.all()[i]).all()])
        # ques.append(models.Option.objects.all().filter(question_link = i).all())
    return render(request, "ques_list.html",
                  context={"ques": ques, "form_name": models.Form.objects.all().filter(id=id).get()})

def dashboard(request):
    return render(request, "dashboard.html")