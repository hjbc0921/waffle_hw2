from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponse
from django.template import loader
  
def post_list(request):
    if not request.user.is_authenticated:
        return redirect('/signin')
    posts = Post.objects.order_by('-created_at')
    return render(request, 'board/post_list.html', {'posts' : posts, 'count' : len(posts)})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'board/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    author = False
    if (request.user == post.author):
        author = True
    next = int(pk)+1
    try:
        Post.objects.get(pk=next)
    except:
        next = 0
    prev = int(pk)-1
    try:
        Post.objects.get(pk=str(prev))
    except:
        prev = 0
    return render(request, 'board/post_detail.html', {'post' : post, 'next':next, 'prev':prev, 'author':author})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'board/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('/posts')
    else:
        return render(request, 'board/post_delete.html', {'title': post.title})
    