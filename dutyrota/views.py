from django.http import HttpResponse
from django.shortcuts import render, Http404, HttpResponseRedirect


def index(request):
    return HttpResponse('Hello World')




