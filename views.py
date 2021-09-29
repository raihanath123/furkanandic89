from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestFun(request):
    return HttpResponse('welcome to cyber square')
def AboutFun(request):
    return HttpResponse('<h1>this is about</h1>')
def hiiiFun(request):
    return HttpResponse('contact')

