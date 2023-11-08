from django.shortcuts import render
from django.http import HttpResponse


def index(reqest):
    return HttpResponse('Hello from the shop app')
