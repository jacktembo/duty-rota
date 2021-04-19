from django.forms import ModelForm
from .models import LeavePermission


class LeavePermissionForm(ModelForm):
    class Meta:
        model = LeavePermission
        fields = '__all__'
