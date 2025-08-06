from django.shortcuts import render

def blog_home_view(request):
    return render(request , 'blog/blog-home.html' )

def blog_single_view(request):
    context = {'title':'wow i changed this title with dynamic url' , 'content':'wow omg i changed the body or bottem of this site how cool this is hmmm.' , 'author':'pedram moz'}
    return render(request , 'blog/blog-single.html' , context )

