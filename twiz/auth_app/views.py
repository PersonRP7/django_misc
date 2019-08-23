from django.shortcuts import render, redirect, HttpResponse

def auth_home(request):
    return HttpResponse("auth home")
