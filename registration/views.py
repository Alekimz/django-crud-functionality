from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

"""
def registration(request):
    return HttpResponse("Welcome to the registration!")

def mypage(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())
# Create your views here.
"""
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def courses(request):
    template = loader.get_template('courses')
    return HttpResponse(template.render())