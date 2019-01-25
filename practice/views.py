from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def practice(request):
    return HttpResponse('Hello World!')

def mydate(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' +str(day))

def myyear(request, year):
    context = {}
    context['year'] = year
    return render(request, 'practice/myyear.html', context)