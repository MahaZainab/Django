from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Post
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

#def index(request):
#    postsQuerySet=Post.objects.all()
#    return render(request, 'index.html', {'posts': postsQuerySet})

    #return HttpResponse("Hello, World");
    #bookQuerySet=Book.objects.all()
    #return render(request, 'index.html', {'books': bookQuerySet})

def detail(request, book_id):
    book=get_object_or_404(Book, id=book_id)
    #book= Book.objects.get(id=book_id)
    return render(request,'detail.html',{'book':book})

    #return HttpResponse(book_id)

def post_detail(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    #post= Post.objects.get(id=post_id)
    return render(request,'detail.html',{'post':post})



from django.http import HttpResponse

def error_400(request, exception):
    return HttpResponse('Cannot find the content!', status=400)

def error_403(request, exception):
    return HttpResponse('Forbidden (403)', status=403)

def error_404(request, exception):
    return HttpResponse('Not Found (404)', status=404)

def error_500(request):
    return HttpResponse('Internal Server Error (500)', status=500)
