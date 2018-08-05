from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Like
from django.utils import timezone
from .forms import PostForm, LoginForm, RegistrationForm, CommentForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'circle/post_list.html', {'posts': posts, 'Like': Like})


def post_new(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES or None)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.publish()
                return redirect('post_list')
        else:
            form = PostForm()
        return render(request, 'circle/post_edit.html', {'form': form})
    else:
        return redirect('login')


def post_edit(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES or None, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_list')
        else:
            form = PostForm(instance=post)
        return render(request, 'circle/post_edit.html', {'form': form})
    else:
        return redirect('login')


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Login successful.')
            return redirect('post_list')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid username or password.')
            form = LoginForm()
            return render(request, 'circle/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'circle/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, 'Username already exists.')
            form = RegistrationForm()
            return render(request, 'circle/register.html', {'form': form})
        else:
            user = User.objects.create_user(username, email, password)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully created user.')
            return redirect('login')
    else:
        form = RegistrationForm()
        return render(request, 'circle/register.html', {'form': form})

def post_detail(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        num_likes = Like.objects.filter(post_pk=pk).count()
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = CommentForm()
        return render(request, 'circle/post_detail.html', {'post': post,'form': form,'num_likes': num_likes})
    else:
        return redirect('login')


@login_required
def user_profile(request):
    posts = Post.objects.filter(author=request.user)
    posts = posts.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'circle/profile.html', {'posts': posts})

@login_required
def like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Like.objects.get_or_create(author=request.user, post_pk=pk)
    return redirect('post_detail', pk=pk)





