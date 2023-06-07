from django.urls import path
from . import views
from django_distill import distill_path
from django.urls import include, path

from main.models import BlogPost



app_name = 'main'

def get_index():
    # this function should return an iterable containing all possible
    # arguments to be passed to your view
    return None

def index(request):
    # your normal view function here
    pass


def get_blog_posts():
    for post in BlogPost.objects.all():
        yield (post.id, )


urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:post_id>/', views.blog_post, name='blog_post'),  # New URL pattern for individual blog posts
    path('blog/new/', views.new_post, name='new_post'),  # New URL pattern for creating new blog posts
    
    distill_path('', views.index, name='index', distill_func=get_index),
    distill_path('blog/', views.blog, name='blog'),
    #distill_path('blog/<int:post_id>/', views.blog_post, name=get_blogposts, name='blog_post'),
    distill_path('blog/<int:post_id>/', views.blog_post, name='blog_post', distill_func=get_blog_posts),
  
    path('markdownx/', include('markdownx.urls')),

]

