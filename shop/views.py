from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Category


def index(reqest):
    courses = Course.objects.all()
    return HttpResponse(courses)
