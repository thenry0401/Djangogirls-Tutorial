from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model

from .models import Post

User = get_user_model()


def post_list(request):
    # return HttpResponse('<html><body>Post List</body></html>')
    # posts변수에 ORM을 이용해서 전체 Post의 리스트(쿼리셋)을 대입
    # posts = Post.objects.all()
    # print(posts)
    # posts = Post.objects.filter(published_date__lte=timezone.now())
    posts = Post.objects.order_by('-created_date')
    context = {
        'title': 'PostList from post-list view',
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context=context)


def post_detail(request, pk):
    # post라는 키값으로 pk또는 id값이 매개변수로 주어진 pk변수와 같은 Post객체를 전달
    context = {
        'post': Post.objects.get(pk=pk),
    }
    return render(request, 'blog/post_detail.html', context)


def post_create(request):
    if request.method == 'GET':
        context = {

        }
        return render(request, 'blog/post_create.html', context)
    elif request.method == 'POST':
        data = request.POST
        title = data['title']
        text = data['text']
        user = User.objects.first()
        post = Post.objects.create(
            title=title,
            text=text,
            author=user,
        )
        return redirect('post_detail', pk=post.pk)
