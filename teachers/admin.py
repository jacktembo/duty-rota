from django.contrib import admin
from .models import Teacher, Supervisor
from dutyrota.utils import *

admin.site.register(Teacher)
admin.site.register(Supervisor)
