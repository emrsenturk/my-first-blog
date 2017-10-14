from django.shortcuts import render
from .models import Post
from django.utils import timezone


def post_list(request):
	return render(request, 'blog/post_list.html',{})

def post_list(request):
	posts = Post.objects.filter(yayinlanma_tarihi__lte=timezone.now()).order_by('yayinlanma_tarihi')
	return render(request,'blog/post_list.html',{'posts':posts})
# Create your views here.
