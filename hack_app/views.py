from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
	if request.method == 'POST':
		h = request.POST['comment']
		p = request.POST['coment']
		a = int(h) * int(p)
		Hack.objects.create(hack=a)
	posts = Hack.objects.all()
	context = {
		'posts':posts,
	}
	return render(request, 'index.html', context)