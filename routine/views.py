from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponse('Hello')


