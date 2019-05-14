from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index1(request):
#     name = request.POST.get('name')
#     return HttpResponse('len is {}'.format(len(name)))

def index2(request):
     age = request.POST.get('age')
     if int(age) >= 18:
        return HttpResponse('Hello')
     else:
         return HttpResponse('Error! So young!')