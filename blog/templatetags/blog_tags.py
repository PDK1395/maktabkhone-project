from django import template
from blog.models import Post , Comment
from blog.models import Category

register = template.Library()

@register.simple_tag(name='total_posts')
def function():
    posts = Post.objects.filter(status = 1).count()
    return posts

@register.simple_tag(name='comments_count')
def function(pid):
    post = Post.objects.get(pk = pid)
    return Comment.objects.filter(post=post.id,approved=True).count()
   

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status = 1)
    return posts

@register.filter
def snippet(value, word_count=10):
    words = value.split()
    if len(words) > word_count:
        return ' '.join(words[:word_count]) + '...'
    return value
'''
@register.filter 
def snippet(value):
    return value[:20]'''

@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts(arg=2):
    posts = Post.objects.filter(status = 1).order_by('published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def post_categories():
    posts = Post.objects.filter(status = 1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories' : cat_dict}