from django.shortcuts import render
from .models import BlogPost

def blogsPost(request):

    blog = BlogPost.objects.all()

    context = {
        'blogs': blog,
    }

    return render(request, 'blog/blog.html', context)