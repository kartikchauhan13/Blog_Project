from django.shortcuts import render
from .models import Post , Category

# Create your views here.b
def home(request):
	posts=Post.objects.all()
	data={
		'posts':posts
	}
	return render(request ,'home.html' ,data)
	
def blog_post(request ,url):
	post=Post.objects.get(url=url)
	return render(request , 'posts.html' ,{'post':post})