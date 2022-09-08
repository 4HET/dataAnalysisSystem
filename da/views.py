from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, '../templates/data_analysis.html', context)


def myData(request):
    return render(request, '../templates/myData.html')