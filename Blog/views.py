from django.shortcuts import redirect, render, get_list_or_404
from .models import *
from django.core.paginator import Paginator


# Create your views here.
def blogList(request):
    try:
        posts = Post.objects.filter(approved=True)
        tags = Tag.objects.all()
    except:
        posts = None
        tags = None
    context={}


    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    objects = paginator.get_page(page_number)

    context['posts'] = objects

    context['tags'] = tags
    return render(request, 'blog/blog-list.html', context)

def tagChoose(request, tag):
    try:
        posts = Post.objects.filter(tags__name=tag)
        tags = Tag.objects.all()
    except:
        posts = None
    context = {}
    context['posts'] = posts
    context['tags'] = tags
    context['currentTag'] = tag
    return render(request, 'blog/blog-list.html', context)

def blogDetail(request, slug):
    post = get_list_or_404(Post, slug=slug)
    if not post[0].approved: return redirect('/')
    
    if request.method == 'POST':
        comment = Comment(post=post[0], user=request.user, text=request.POST['comment'])
        comment.save()
        return redirect('/blog/post/%s' % slug)

    context = {'post': post[0]}

    return render(request, 'blog/blog-detail.html', context)


def blogSearch(request):
    context = {}
    tags = Tag.objects.all()
    context['tags'] = tags
    if request.method == 'POST':
        search = request.POST['search']
        if not search: 
            return render(request, 'blog/blog-list.html', context)
        try:
            posts = Post.objects.filter(title__contains=search)
        except:
            return render(request, 'blog/blog-list.html', context)
        if posts: 
            context['posts'] = posts
    return render(request, 'blog/blog-list.html', context)
        

def blogSearchByAuthor(request, username):
    context = {} 
    context['tags'] = Tag.objects.all()
    context['posts'] = Post.objects.filter(author__username=username)
    return render(request, 'blog/blog-list.html', context)