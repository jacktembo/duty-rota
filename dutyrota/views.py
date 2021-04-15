from django.http import HttpResponse
from django.shortcuts import render, Http404, HttpResponseRedirect


def index(request):
    return HttpResponse('Welcome to the HomePage Of The Duty Roata')
