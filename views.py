# blogapp/views.py

from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.decorators import login_required

@login_required
def create_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user  # Current logged-in user

        blog = Blog.objects.create(title=title, content=content, author=author)
        # Optionally, you can redirect to a success page or the blog detail view
        return redirect('blog-detail', pk=blog.pk)

    return render(request, 'blog/create_blog.html')

