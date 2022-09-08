# Create your views here.
from audioop import reverse

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import register


@register.filter
def get_range(value):
    return range(value)



def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    # return redirect(reverse("myData:index")
    return render(request, '../templates/myData.html', context)