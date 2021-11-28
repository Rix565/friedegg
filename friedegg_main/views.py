from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from .models import Post


from django.template import loader

def index(request):
    latest_public_posts = Post.objects.order_by('-published_date')[:5]
    template = loader.get_template('friedegg_main/index.html')
    context = {
        'latest_public_posts': latest_public_posts,
    }
    return HttpResponse(template.render(context, request))
def post_view(request, postid):
    try:
        post = Post.objects.get(id=postid)
    except Post.DoesNotExist:
        raise Http404()
    template = loader.get_template('friedegg_main/post-view.html')
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))
