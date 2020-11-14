from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import Post,Comment,MarketPost,PostAgriProblem
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin,UserPassesTestMixin
from .forms import *
from .forms import CommentForm ,AgriCommentForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def main_home_page(request):
    return render(request,'home_main_page.html',{"title":"Home Page"})

def agridoctor_home(request):
    posts = PostAgriProblem.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context ={
        'posts':posts,
        'title':'blog_home',
    }
    return render(request,'agridoctor/home.html',context)
"""
def blog_detail(request, pk):
    posts = Post.objects.get(pk=pk)
    context = {
        "posts":posts
    }
    return render(request,'blog/blog_detail.html',context)
"""

def agridoctor_detail(request, pk):
    post = get_object_or_404(PostAgriProblem, pk=pk)
    comments =post.comments.filter(active=True,parent__isnull=True)
    if request.method == 'POST':
        comment_form = AgriCommentForm(data =request.POST )
        if comment_form.is_valid():
            parent_obj = None
            try:
                 parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id=None
            if parent_id:
                 parent_obj=AgriComment.objects.get(id=parent_id) 
                 if parent_obj:
                     reply_comment = comment_form.save(commit=False)
                     reply_comment.parent = parent_obj
            new_comment =comment_form.save(commit=False) 
            new_comment.post=post
            new_comment.save()
            return redirect('agridoctor_detail',pk)
    else:
        comment_form =  AgriCommentForm()

    context = {
        "posts":post,
        "comments":comments,
        "comment_form":comment_form
    }

    return render(request,'agridoctor/agridoctor_detail.html',context)

    



def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments =post.comments.filter(active=True,parent__isnull=True)
    if request.method == 'POST':
        comment_form = CommentForm(data =request.POST )
        if comment_form.is_valid():
            parent_obj = None
            try:
                 parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id=None
            if parent_id:
                 parent_obj=Comment.objects.get(id=parent_id) 
                 if parent_obj:
                     reply_comment = comment_form.save(commit=False)
                     reply_comment.parent = parent_obj
            new_comment =comment_form.save(commit=False) 
            new_comment.post=post
            new_comment.save()
            return redirect('blog_detail',pk)
    else:
        comment_form =  CommentForm()

    context = {
        "posts":post,
        "comments":comments,
        "comment_form":comment_form
    }
    return render(request,'blog/blog_detail.html',context)






def home(request):
    posts = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context ={
        'posts':posts,
        'title':'blog_home',
    }
    return render(request,'blog/home.html',context)

#listing the blog post
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model =Post
    template_name = 'blog/post_detail.html'



class PostCreateView(LoginRequiredMixin, CreateView):
    model =Post
    template_name = 'blog/post_form.html'
    fields = ['title','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AgridoctorCreateView(LoginRequiredMixin, CreateView):
    model =PostAgriProblem
    template_name = 'agridoctor/agridoctor_form.html'
    fields = ['image','description']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#fields = ['type_of_item','description','image','quantity']
                 

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model =Post
    template_name = 'blog/post_form.html'
    fields = ['title','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProblemUpdateView(LoginRequiredMixin, UpdateView):
    model = PostAgriProblem
    template_name = 'agridoctor/agridoctor_form.html'
    fields = ['image','description']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
       

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = "/"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# market place home page list views
def market_home(request):
    posts = MarketPost.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context ={
        'posts':posts,
        'title':'blog_home',
    }
    return render(request,'market/home.html',context)

def market_detail(request, pk):
    posts = MarketPost.objects.get(pk=pk)
    context = {
        'posts':posts
    }
    return render(request,'market/market_detail.html',context)

class MarketCreateView(LoginRequiredMixin, CreateView):
    model = MarketPost
    template_name = 'market/market_form.html'
    fields = ['type_of_item','description','contact','image','location','quantity']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MarketUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = MarketPost
    template_name = 'market/market_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): 
        post =self.get_object()   
        if self.request.user == post.author:
            return True
        return False    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): 
        post =self.get_object()   
        if self.request.user == post.author:
            return True
        return False           
class MarketDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model =MarketPost
    success_url = "/"
    template_name = 'market/market_confirm_delete.html' 
    def test_func(self): 
        post =self.get_object()   
        if self.request.user == post.author:
            return True
        return False          

class ProblemDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = PostAgriProblem
    success_url = "/"
    template_name = 'agridoctor/problem_confirm_delete.html' 
    def test_func(self): 
        post =self.get_object()   
        if self.request.user == post.author:
            return True
        return False          



#view about
def about(request):
    context={
        'title':'blog-about'
    }
    return render(request,'blog/about.html',context)    