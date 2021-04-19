from django.http import HttpResponse
from django.shortcuts import render, Http404, HttpResponseRedirect
from .models import LeavePermission
from datetime import datetime, date


def index(request):
    return HttpResponse('Helllo World')


def permission(request):
    if request.method != 'POST':
        return render(request, 'index.html')
    else:

        """Permission request to leave campus"""
        captured = request.POST  # We capture data from the form.
        leave_permission = LeavePermission(
            pupil_name=captured['Name'],
            pupil_id=564667,
            pupil_email=captured['Email'],
            pupil_phone=captured['Number'],
            reason=captured['SingleLine'],
            explanation=captured['MultiLine'],
            date_requested=datetime.today(),
            date_leaving=date.fromisoformat(captured['Date'][::-1]),
            time_leaving=datetime.time(
                int(captured['Time_hours']), int(captured['Time_minutes'])),
            date_back=date.fromisoformat(captured['DateTime_date'][::-1])

        )
        leave_permission.save()
