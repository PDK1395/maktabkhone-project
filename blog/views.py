from django.shortcuts import render , get_object_or_404
from blog.models import Post
def blog_home_view(request):
    posts = Post.objects.filter(status =1)
    context = {'posts' : posts}
    return render(request , 'blog/blog-home.html' , context)

def blog_single_view(request,pid):
    posts = Post.objects.filter(status =1)
    post = get_object_or_404(posts,pk=pid)
    next_post = posts.filter(id__gt=post.id).order_by('id').first()
    prev_post = posts.filter(id__lt=post.id).order_by('-id').first()
    context = {'post' : post , 'posts':posts ,'next_post': next_post , 'prev_post': prev_post}
    return render(request , 'blog/blog-single.html' , context )

def test(request,pid):
#    post = Post.objects.get(id=pid)
    posts = get_object_or_404(Post,pk=pid)
    context = {'posts':posts}
    return render(request , 'test.html' , context)