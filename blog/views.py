from multiprocessing import context
from django.shortcuts import render, HttpResponse
from blog.models import Post


# Create your views here.
def bloghome(request):
    allpost = Post.objects.all()
    # print(allpost)
    context = {'allpost': allpost}
    return render(request, 'blog/bloghome.html', context)
    # return HttpResponse("This is bloghome")


def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    # print(post)
    return render(request, 'blog/blogpost.html', context)
    # return HttpResponse(f"This is Blogpost {slug}")
