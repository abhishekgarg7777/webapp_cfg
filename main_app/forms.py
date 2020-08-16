from django import forms

from .models import Form,Type,Form,Question,Option

class CreateCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields =[
            "name",
            "budget",
        ]
class Form1(forms.Form):
    name = forms.CharField()    
    category = forms.ModelChoiceField(queryset=None) 

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(Form1, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Question.objects.filter(user=self.user)
