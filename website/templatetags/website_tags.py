from django import template
from blog.models import Post
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('website/latest-from-our-blog.html')
def latest_from_blog(arg=6):
    posts = Post.objects.filter(published_date__lte = timezone.now() , status =1).order_by('published_date')[:arg]
    return {'posts':posts}