from django.shortcuts import render
from .models import Artist
# Create your views here.

def index(request):
	template = 'index.html'
	context = {}
	return render(request, template,context)

def artists(request):
	template = 'artists.html'
	artist_objects = Artist.objects.all()
	context = {
	'artists': artist_objects, 
	}
	return render(request, template, context)