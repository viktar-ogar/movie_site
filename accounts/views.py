from django.shortcuts import render
from django.http import HttpRequest


def loginPage(request):
    return render(request, "accounts/login.html")

def registerPage(request):
    context = {}
    return render(request, "accounts/register.html", context)