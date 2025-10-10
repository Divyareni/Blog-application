from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from .models import Post
from django.core.paginator import Paginator
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

posts = [
    {
        "id": 1,
        "title": "My book",
        "content": "This is a pre-requisite"
    },
    {
        "id":2,
        "title": "My book-2",
        "content": "This is a beginner book"
    }
]

categories = [
    'programming',
    'Food',
    'Travel'

]

def hello_world(request):
    html = ""
    for post in posts:
        html+= f'''
               <div>
               <h1>{post['id']}</h1>
               <p>{post['content']}</p>
               </div>

'''
    return HttpResponse(html)


def post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            posturl = reverse('post', args=[id])
            return HttpResponseRedirect(posturl)
    form = CommentForm()
    context = {
            'post_dict': post,
            'categories': categories,
            'form':form
    }
    return render(request, 'posts/post.html', context)
    

def my_function(request):
    all_posts = Post.objects.all().order_by('-id')
    paginator = Paginator(all_posts, 2)
    page_number = request.GET.get('p',3)
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    print(page_obj.has_previous())
    print(all_posts)
    context = {
        'posts': page_obj,
        'username': 'divya',
        'categories': categories,
    }
    return render(request, 'posts/index.html', context)



def google(request):
    return HttpResponseRedirect('https://google.com')



