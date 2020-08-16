from django.contrib import admin

# Register your models here.
from .models import Type,Form,Question,Option
# Register your models here.

admin.site.register(Type)
admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Option)
