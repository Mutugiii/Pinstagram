from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    '''Main view function for the start page'''
    return render(request, 'index.html')

