from django.forms import ModelForm
from .models import LeavePermission


class PermissionForm(ModelForm):
    class Meta:
        model = LeavePermission
