from django.contrib import admin
from .models import Teacher, Supervisor
from dutyrota.utils import *

admin.site.register(Teacher)
admin.site.register(Supervisor)
admin.site.register(Year)
admin.site.register(Month)
admin.site.register(Week)
admin.site.register(Day)
admin.site.register(Term)
admin.site.register(Gender)
admin.site.register(Title)
