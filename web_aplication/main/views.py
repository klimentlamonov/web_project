from django.shortcuts import render
from .models import Comments

def index(request):
	comments = Comments.objects.all()
	return render(request, 'main/index.html', {'comments': comments})


def about(request):
	return render(request, 'main/about.html')