from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Салам')


def group_posts(request, slug):
    return HttpResponse(f'Здесь будут посты от {slug}')
