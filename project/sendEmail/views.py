# from django.shortcuts import render
from django.http import HttpResponse


def send_email(request):
    return HttpResponse("sendEmail")
