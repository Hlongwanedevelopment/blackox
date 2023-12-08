from django.urls import reverse 
from django.shortcuts import render, redirect
from website.models import (
    Cattle,
    Contact,
    Post,
    JobPost,
    FarmOperation
)
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
import datetime
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
# Create your views here.

def indcnt(request):
    post = Post.objects.all()[:4]
    operations = FarmOperation.objects.all()
    return render(request, "website/index.html", {
        "posts": post,
        "operations": operations
    })

def landing(request):
    operations = FarmOperation.objects.all()
    # Pass Data into the context dictionary
    context = {
        'operations':operations
    }
    return render(request, "website/landing.html", context)

def ourfarms(request):
    operations = FarmOperation.objects.all()
    return render(request, "website/ourfarms.html", {
        "operations": operations
    })

def farmoperations(request):
    operations = FarmOperation.objects.all()
    return render(request, "website/farmsoperations.html", {
        "operations": operations
    })

def farmoperationdetail(request, pk):
    operation = FarmOperation.objects.get(pk=pk)
    operations = FarmOperation.objects.all()
    return render(request, "website/operationdetail.html", {
        "operation": operation,
        "operations": operations
    })

def aboutfarm(request):
    operations = FarmOperation.objects.all()
    return render(request, "website/about.html", {
        "operations": operations
    })

def contact(request):
    if request.method == "GET":
        operations = FarmOperation.objects.all()
        return render(request, "website/contact.html", {
            "operations": operations
        })
    
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        phonenumber = request.POST.get("phonenumber")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if not email:
            messages.error(request, "Email is required to proceed")
            return redirect(reverse("website:contact"))
        
        try:
            c = Contact.objects.create(
                first_name = firstname,
                last_name = lastname,
                message = message,
                email = email,
                tel= phonenumber
            )

            send_mail(
                "Thank you for contacting us.",
                "This is an automated notifier. Our Team will be intouch with you shortly",
                "test@com.com",
                [email],
                fail_silently=True
            )

            messages.success(request, "Thank you for your request")

            return redirect(reverse("website:contact"))
        except BadHeaderError as b:
            messages.error(request, f"{b}")

            return redirect("website:contact")
            

def careers(request):
    posts = JobPost.objects.all()
    operations = FarmOperation.objects.all()
    return render(request, "website/careers.html", {
        'posts':posts,
        "operations": operations
        })

def careerdetail(request, pk):
    post = JobPost.objects.get(pk=pk)
    operations = FarmOperation.objects.all()
    return render(request, "website/careerdetail.html", {
        "post": post,
        "operations": operations
    })

def applytopost(request, pk):
    if request.method == "GET":
        operations = FarmOperation.objects.all()
        post = JobPost.objects.get(pk=pk)
        return render(request, "website/applytopost.html", {
            "post":post,
            "operations": operations
        })
    
    if request.method == "POST":
        pass
    
def FAQ(request):
    operations = FarmOperation.objects.all()
    return render(request, "website/faq.html", {
        "operations": operations
    })

# blog class based views
class Blog(ListView):
    model = Post
    template_name = 'website/blog-home-2.html'
    ordering = ['-post_time']

    def get_context_data(self, **kwargs):
        # headerpost = Post.objects.get()
        now = datetime.datetime.today()
        print(now)
        headerpost = Post.objects.all()[:1]
        operations = FarmOperation.objects.all()
        context = super().get_context_data(**kwargs)
        context["header"] = headerpost
        context["operations"] = operations
        return context

class Blogdetail(DetailView):
    model = Post
    template_name = 'website/blog-post.html'

    def get_context_data(self, **kwargs):
        data = get_object_or_404(Post, id=self.kwargs['pk'])
        recentposts = Post.objects.all().order_by('-post_time').exclude(pk=data.pk)[:3]
        operations = FarmOperation.objects.all()
        print(recentposts)
        context = super().get_context_data(**kwargs)
        context["recentposts"] = recentposts
        context["operations"] = operations
        return context

