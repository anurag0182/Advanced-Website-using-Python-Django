from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog, Category, Comment


def home(request):
    query = request.GET.get('q')

    posts = Blog.objects.all().order_by('-created_at')

    if query:
        posts = posts.filter(title__icontains=query)

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    featured = Blog.objects.filter(is_featured=True)[:5]
    trending = Blog.objects.all().order_by('-created_at')[:5]
    categories = Category.objects.all()

    return render(request, 'home.html', {
        'page_obj': page_obj,
        'featured': featured,
        'trending': trending,
        'categories': categories
    })


def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)

    trending = Blog.objects.exclude(id=post.id).order_by('-created_at')[:5]
    suggested = Blog.objects.exclude(id=post.id).order_by('-created_at')[5:11]

    if request.method == "POST":
        Comment.objects.create(
            post=post,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            comment=request.POST.get('comment')
        )

    comments = post.comments.all().order_by('-created_at')

    return render(request, 'blog_detail.html', {
        'post': post,
        'trending': trending,
        'suggested': suggested,
        'comments': comments
    })


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Blog.objects.filter(category=category).order_by('-created_at')

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'category.html', {
        'category': category,
        'page_obj': page_obj
    })

