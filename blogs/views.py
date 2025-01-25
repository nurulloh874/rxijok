from django.shortcuts import redirect, render
from .models import Blog, BlogImage, Category, Comment
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm

# Create your views here.

def blog_page(request):
    bloglar = Blog.objects.all()
    kategoriyalar = Category.objects.all()

    context = {
        'bloglar': bloglar,
        'kategoriyalar': kategoriyalar
    }
    return render(request, template_name='index.html', context=context)


def about_page(request):
    return render(request, template_name='about.html')


def contact_page(request):
    return render(request, template_name='contact.html')

    

def blog_detail_page(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    kategoriyalar = Category.objects.all()
    comments = blog.comment_set.all()  # Blogga tegishli izohlarni olish

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('blog_detail', blog_id=blog.pk)  # Yangi izohdan keyin sahifani yangilash
    else:
        form = CommentForm()

    context = {
        'blog': blog,
        'kategoriyalar': kategoriyalar,
        'comments': comments,
        'form': form,
    }

    return render(request, 'post.html', context)
