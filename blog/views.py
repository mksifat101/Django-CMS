from django.core import paginator
from django.shortcuts import get_object_or_404, render
from blog.models import Category, SubCategory, Post
from banner.models import HomeBanner1, HomeBanner2
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def home(request):
    top_post = Post.objects.all().order_by('-create_date')[0:8]
    post = Post.objects.all().order_by('-create_date')
    category = Category.objects.all().order_by('-create_date')
    popular = Post.objects.annotate().filter()[0:4]
    banner1 = HomeBanner1.objects.all()[0:1]
    banner2 = HomeBanner2.objects.all()[0:1]
    # Pagination
    paginator = Paginator(post, 6)
    page = request.GET.get('page')
    paged_post = paginator.get_page(page)
    cat = Category.objects.all()
    context = {
        'top_post': top_post,
        'category': category,
        'post': paged_post,
        'popular': popular,
        'banner1': banner1,
        'banner2': banner2,
        'cat': cat,
    }
    return render(request, 'blog/home.html', context)


# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['now'] = timezone.now()
#     context.update(self.extra_context)
#     return context


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    post = Post.objects.all().filter(category=category)
    post_cat = Category.objects.get(slug=slug)
    popular = Post.objects.annotate().filter()[0:4]
    nav = Category.objects.all().order_by('-create_date')
    # Pagination
    paginator = Paginator(post, 6)
    page = request.GET.get('page')
    paged_post = paginator.get_page(page)
    cat = Category.objects.all()
    banner1 = HomeBanner1.objects.all()[0:1]
    banner2 = HomeBanner2.objects.all()[0:1]
    context = {
        'post': paged_post,
        'post_cat': post_cat,
        'popular': popular,
        'cat': cat,
        'banner1': banner1,
        'banner2': banner2,
        'nav': nav,
    }
    return render(request, 'blog/category.html', context)


def single(request, category_slug, post_slug):
    single = Post.objects.get(category__slug=category_slug, slug=post_slug)
    category = Category.objects.all()
    popular = Post.objects.annotate().filter()[0:4]
    banner1 = HomeBanner1.objects.all()[0:1]
    banner2 = HomeBanner2.objects.all()[0:1]
    nav = Category.objects.all().order_by('-create_date')
    context = {
        'single': single,
        'popular': popular,
        'category': category,
        'banner1': banner1,
        'banner2': banner2,
        'nav': nav,
    }
    return render(request, 'blog/single.html', context)
