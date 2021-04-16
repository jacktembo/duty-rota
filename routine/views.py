from django.shortcuts import render, reverse, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from datetime import date, datetime, time, timedelta
from .models import DutyRota, Announcement
from teachers.models import Teacher, Supervisor


today = date.today()  # Today's date
tomorrow = today + timedelta(days=1)  # Tomorrows's date

current_year = today.year

def index(request):
    context = {}
    return render(request, 'index.html', context)


def today_rota(request):
    # Duty rota that has today's date
    today_duty_rota = get_object_or_404(DutyRota, date=today)
    teachers_on_duty = today_duty_rota.teachers.all()
    supervisors_on_duty = today_duty_rota.supervisors.all()


def tomorrow_rota(request):
    #Tomorrow's duty rota
    tomorrow_duty_rota = get_object_or_404(DutyRota, date=tomorrow)
    teachers_on_duty_tomorrow = tomorrow_duty_rota.teachers.all()
    supervisors_on_duty_tomorrow = tomorrow_duty_rota.supervisors.all()


def annoucements(request):
    #Announcements to either pupils or staff
    annoucements = get_list_or_404(Announcement)






