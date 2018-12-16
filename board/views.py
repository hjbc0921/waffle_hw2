from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponse
from django.template import loader
  
def post_list(request):
    if not request.user.is_authenticated:
        return redirect('/signin')
    posts = Post.objects.order_by('-created_at')
    mine = Post.objects.filter(author=request.user)
    return render(request, 'board/post_list.html', {'posts' : posts, 'count' : len(posts), 
                            'user' : request.user.username, 'mine' : mine, 'mcount' : len(mine)})

def post_create(request):
    if request.method == "POST":
        post = Post(title=request.POST['title'], content=request.POST['content'], author=request.user)
        post.save()
        return redirect('post_detail', pk=post.pk)
    return render(request, 'board/post_edit.html', {'new':True, 'title':'', 'content':''})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    author = False
    if (request.user == post.author):
        author = True
    posts = Post.objects.order_by('pk')
    index = 0
    for p in posts:
        if (int(p.pk) == int(pk)):
            break
        index += 1
    if (index == 0):
        prev = 0
    else:
        prev = posts[index-1].pk
    if (index == len(posts)-1):
        next = 0
    else:
        next = posts[index+1].pk
    return render(request, 'board/post_detail.html', {'post' : post, 'next':next, 'prev':prev, 'author':author})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.title=request.POST['title']
        post.content=request.POST['content']
        post.save()
        return redirect('post_detail', pk=post.pk)
    return render(request, 'board/post_edit.html', {'new': False, 'title': post.title, 'content': post.content})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('/posts')
    else:
        return render(request, 'board/post_delete.html', {'title': post.title})
    