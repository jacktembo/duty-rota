from django.http import HttpResponse
from django.shortcuts import render, Http404, HttpResponseRedirect


def index(request):
    context = {}
    return render(request, 'index.html', context)




