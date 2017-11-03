from django.http import HttpResponse
from django.shortcuts import render

from .forms import BookForm


def formDetail(request):
    detail = BookForm() 
    return HttpResponse(detail)
