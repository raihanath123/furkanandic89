from django.shortcuts import render
from django.http import HttpResponse
def IndexFun(request):
 return render(request,'index.html')
def AboutFun(request):
    return render(request,'about.html')
def contactFun(request):
    return render(request,'contact.html')
