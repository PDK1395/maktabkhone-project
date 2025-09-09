from django.shortcuts import render , get_object_or_404
from blog.models import Post
from django.utils import timezone

def blog_home_view(request):
    posts = Post.objects.filter(published_date__lte = timezone.now() , status =1)
    context = {'posts' : posts}
    return render(request , 'blog/blog-home.html' , context)


def blog_single_view(request,pid):
    posts = Post.objects.filter(published_date__lte = timezone.now() , status =1)
    post = get_object_or_404(posts,pk=pid)
    post.counted_view += 1
    post.save()  
    next_post = posts.filter(id__gt=post.id, status=1).order_by('published_date').first()
    prev_post = posts.filter(id__lt=post.id, status=1).order_by('-published_date').first()
    context = {'post' : post ,
               'next_post': next_post , 
               'prev_post': prev_post
    }
    return render(request , 'blog/blog-single.html' , context )


def blog_category(request,cat_name):
    posts = Post.objects.filter(status = 1)
    posts = posts.filter(category__name = cat_name)
    context = {'posts' : posts}
    return render(request,'blog/blog-home.html',context)


def test(request):
    return render(request,'test.html')

