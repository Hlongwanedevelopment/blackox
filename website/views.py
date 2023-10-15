from typing import Any
from django.shortcuts import render
from website.models import (
    Breed,
    Cattle,
    Sheep,
    Contact,
    Post,
    JobPost
)
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
import datetime
# Create your views here.


def landing(request):
    cattles = Cattle.objects.all()[:3]
    # Pass Data into the context dictionary
    context = {
        'cattles': cattles
    }
    return render(request, "website/landing.html", context)

def ourbreed(request):
    return render(request, "website/ourbreed.html", {})

def aboutfarm(request):
    return render(request, "website/about.html", {})

def contact(request):
    return render(request, "website/contact.html", {})

def careers(request):
    posts = JobPost.objects.all()
    return render(request, "website/careers.html", {'posts':posts})

def FAQ(request):
    return render(request, "website/faqs.html", {})

# blog class based views
class Blog(ListView):
    model = Post
    template_name = 'website/blog.html'
    ordering = ['-post_time']

    def get_context_data(self, **kwargs):
        # headerpost = Post.objects.get()
        now = datetime.datetime.today()
        print(now)
        headerpost = Post.objects.all()[:1]
        context = super().get_context_data(**kwargs)
        context["header"] = headerpost
        return context

class Blogdetail(DetailView):
    model = Post
    template_name = 'website/blogdetail.html'

    def get_context_data(self, **kwargs):
        data = get_object_or_404(Post, id=self.kwargs['pk'])
        recentposts = Post.objects.all().order_by('-post_time').exclude(pk=data.pk)[:3]
        print(recentposts)
        context = super().get_context_data(**kwargs)
        context["recentposts"] = recentposts
        return context

class CattleDetail(DetailView):
    model = Cattle
    template_name = "website/detail.html"