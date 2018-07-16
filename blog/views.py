from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    url1 = 'https://www.youtube.com/watch?v=DHdi6HhbvfQ'
    t = url1.split('watch?v=')
    t1 = t[0]+'embed/'
    t2 = t[1].split('&')
    t3 = t1+t2[0]
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'url': t3})