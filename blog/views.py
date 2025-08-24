from django.shortcuts import render , get_object_or_404
from blog.models import Post
def blog_home_view(request):
    posts = Post.objects.filter(status =1)
    context = {'posts' : posts}
    return render(request , 'blog/blog-home.html' , context)

def blog_single_view(request):
    context = {'title':'wow i changed this title with dynamic url' , 'content':'wow omg i changed the body or bottem of this site how cool this is hmmm.' , 'author':'pedram moz'}
    return render(request , 'blog/blog-single.html' , context )

def test(request,pid):
#    post = Post.objects.get(id=pid)
    post = get_object_or_404(Post,pk=pid)
    context = {'pid':pid}
    return render(request , 'test.html' , context)