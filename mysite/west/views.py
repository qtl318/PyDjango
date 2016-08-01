# -*- coding: utf-8 -*-
#from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from west.models import charname

def first_page(request):
	return HttpResponse("<p>番茄土豆</p>")

def star(request):
	star_list = charname.objects.all()
	star_str = map(str,star_list)
	return HttpResponse("<p>" + ' '.join(star_str) + '</p>')

#from django.http import HttpResponse
from django.shortcuts import render
 
def templay(request):
    context          = {}
    context['label'] = 'Hello World!'
    return render(request, 'templay.html', context)