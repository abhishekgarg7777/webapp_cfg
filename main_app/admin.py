from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.

admin.site.register(Type)
admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Project)
admin.site.register(Option)
