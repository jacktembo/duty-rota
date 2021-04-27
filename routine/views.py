from django.shortcuts import render, reverse, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from datetime import date, datetime, time, timedelta
from .models import DutyRota, Announcement
from django.contrib.auth.decorators import login_required


today = date.today()  # Today's date
tomorrow = today + timedelta(days=1)  # Tomorrows's date

current_year = today.year


@login_required
def index(request):
    context = {}
    return render(request, 'routine/dashboard.html', context)


@login_required
def today_rota(request):
    # Duty rota that has today's date
    today_duty_rota = get_object_or_404(DutyRota, date=today)
    teachers_on_duty = today_duty_rota.teachers.all()
    supervisors_on_duty = today_duty_rota.supervisors.all()
    tomorrow_duty_rota = get_object_or_404(DutyRota, date=tomorrow)
    teachers_on_duty_tomorrow = tomorrow_duty_rota.teachers.all()
    supervisors_on_duty_tomorrow = tomorrow_duty_rota.supervisors.all()
    context = {
        'tomorrow_rota': tomorrow_duty_rota, 'tomorrow_teachers': teachers_on_duty_tomorrow,
        'tomorrow_supervisors': supervisors_on_duty_tomorrow,
        'rota': today_duty_rota, 'teachers': teachers_on_duty,
        'supervisors': supervisors_on_duty,
    }
    return render(request, 'routine/today_rota.html', context)


@login_required
def annoucements(request):
    # Announcements to either pupils or staff
    announcements = Announcement.objects.order_by('-published_date_time')[:10]
    context = {
        'announcements': announcements
    }
    return render(request, 'routine/announcements.html', context)


@login_required
def leave_permission(request):
    return HttpResponse('Hello LeavePermission')


def check_who(request):
    """This view checks who will be on duty on a selected date"""
    if request.method != 'POST':
        return render(request, 'check_who.html')
    else:
        selected_date = datetime.fromisoformat(request.POST['date'])
        duty_rota = get_object_or_404(DutyRota, date=selected_date)
        teachers_on_duty = duty_rota.teachers.all()
        supervisors_on_duty = duty_rota.supervisors.all()
        context = {
            'date': selected_date, 'rota': duty_rota,
            'teachers': teachers_on_duty,
            'supervisors': supervisors_on_duty
        }

        return render(request, 'check_who_results.html', context)
