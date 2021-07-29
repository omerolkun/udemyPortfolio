from django import http
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def employee(request):
    return HttpResponse("employee page")

def profile(request):
    return HttpResponse("profile page")