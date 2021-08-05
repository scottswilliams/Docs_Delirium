"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, Http404
from django.views import generic
from .models import Post
from random import randint

def cartoon_detail(request, pk):
    assert isinstance(request, HttpRequest)
    newest_cartoon_id = Post.objects.latest('id').id
    random_id = randint(1, newest_cartoon_id)
    try:
        cartoon = get_object_or_404(Post, id=pk)
    except:
        return Http404("No cartoon with this ID exists. Come back in a few years.")
    return render(request,
        'app/index.html', 
        {
            'cartoon': cartoon,
            'cartoon_id': str(cartoon.id),
            'title': """Doc's Delirium #""" + str(pk),
            'year':datetime.now().year,
            'prev_cartoon': str(max(pk-1, 1)),
            'next_cartoon': str(min(pk+1, Post.objects.latest('id').id)),
            'last_cartoon': str(Post.objects.latest('id').id),
            'published_date': cartoon.published_date,
            'random_cartoon': random_id
        }
    )

def index(request):
    """Renders the  homepage, which is the first cartoon."""
    assert isinstance(request, HttpRequest)
    latest_cartoon = Post.objects.latest('id')
    try:
        cartoon = get_object_or_404(Post, id=1)
    except:
        return Http404("No cartoon with this ID exists. Come back in a few years.")
    random_id = randint(1, latest_cartoon.id)
    
    return render(
        request,
        'app/index.html',
        {
            'cartoon': cartoon,
            'cartoon_id': str(cartoon.id),
            'title': """Doc's Delirium""",
            'year':datetime.now().year,
            'prev_cartoon': '1',
            'next_cartoon': '2',
            'last_cartoon': str(latest_cartoon.id),
            'published_date': cartoon.published_date,
            'random_cartoon': random_id

        }
    )


def about(request):
    assert isinstance(request, HttpRequest)
    newest_cartoon_id = Post.objects.latest('id').id
    random_id = randint(1, newest_cartoon_id)
    """Renders the 'about' page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':"A Short History of Doc's Delirium",
            'year':datetime.now().year,
            'first_cartoon': '1',
            'random_cartoon': random_id,
            'last_cartoon': str(newest_cartoon_id)
        }
    )
