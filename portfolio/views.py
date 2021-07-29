from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        'thanks_to' : ['buket','cem','yagiz','muccio']

    }
    return render(request, "index.html",context)

def about(request):
    return render(request,'about.html')


def contactus(request):
    return render(request,'contactus.html')
