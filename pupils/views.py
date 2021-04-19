from django.http import HttpResponse
from django.shortcuts import render, Http404, HttpResponseRedirect
from .models import LeavePermission
from datetime import datetime, date
from .forms import LeavePermissionForm


def index(request):
    return HttpResponse('Helllo World')


def permission(request):

    if request.method != 'POST':
        form = LeavePermissionForm()

        return render(request, 'leave.html', {'form': form})
    else:
        form = LeavePermissionForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse('something went wrong')
