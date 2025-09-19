from django.shortcuts import render , get_object_or_404
from blog.models import Post , Comment
from django.utils import timezone
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from blog.forms import CommentForm
from django.contrib import messages

def blog_home_view(request,cat_name=None,auth_name = None,tag_name = None):
    posts = Post.objects.filter(published_date__lte = timezone.now() , status =1)
    
    if cat_name:
        posts = posts.filter(category__name = cat_name)
    if auth_name:
        posts = posts.filter(author__username = auth_name)                 
    if tag_name:
        posts = posts.filter(tags__name__in=[tag_name])

    
    posts = Paginator(posts,2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.page(1)
    except EmptyPage:
        posts = posts.page(1)
    
    context = {'posts' : posts}
    return render(request , 'blog/blog-home.html' , context)


# in zir rah dovome hamin balayy hast ke age dost dashtim va benazaremon behtar bood mitoni onjory ham benevisim
'''
def blog_home_view(request,**kwargs):
    posts = Post.objects.filter(published_date__lte = timezone.now() , status =1)
    
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('auth_name'):
        posts = posts.filter(author__username = kwargs['auth_name'])
        
    context = {'posts' : posts}
    return render(request , 'blog/blog-home.html' , context)
'''


def blog_single_view(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment created successfully')
        else:
            messages.add_message(request,messages.ERROR,'your message had problem creating')
    posts = Post.objects.filter(published_date__lte = timezone.now() , status =1)
    post = get_object_or_404(posts,pk=pid)
    comments = Comment.objects.filter(post=post.id , approved=True)
    post.counted_view += 1
    post.save()  
    next_post = posts.filter(id__gt=post.id, status=1).order_by('published_date').first()
    prev_post = posts.filter(id__lt=post.id, status=1).order_by('-published_date').first()
    form = CommentForm()
    context = {'post' : post ,
               'next_post': next_post , 
               'prev_post': prev_post , 
               'comments' : comments ,
               'form' : form ,
    }       
    form = CommentForm()
    return render(request , 'blog/blog-single.html' , context )


def blog_category(request,cat_name):
    posts = Post.objects.filter(status = 1)
    posts = posts.filter(category__name = cat_name)
    context = {'posts' : posts}
    return render(request,'blog/blog-home.html',context)

def blog_search(request):
    posts = Post.objects.filter(status = 1)
    if request.method == 'GET':
        search_term = request.GET.get('s')
        if search_term:
            posts = posts.filter(title__icontains  = search_term )
             
    context = {'posts' : posts }
    return render(request , 'blog/blog-home.html' , context)


