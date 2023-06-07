from django.shortcuts import render, get_object_or_404,redirect

from django.http import HttpResponse

from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt
from .models import BlogPost
from .forms import BlogPostForm
from django.utils import timezone


def index(request):
    return render(request, 'main/index.html')


def blog(request):
    posts = BlogPost.objects.order_by('-pub_date')
    return render(request, 'main/blog.html', {'posts': posts})

def blog_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'main/blog_post.html', {'post': post})

def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('main:blog_post', post_id=post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'main/new_post.html', {'form': form})


