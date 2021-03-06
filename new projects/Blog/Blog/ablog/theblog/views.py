from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm,UpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



#def home(request):
 #   return render(request,'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering= ['-id']
    ordering= ['-post_date']

    #def get_context_data(self, *args,**kwargs):
    #    cat_menu = Category.objects.all()
    #    context = super(HomeView,self).get_context_data(*args,**kwargs)
    #    context ['cat_menu'] = cat_menu
    #    return context

    


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(LoginRequiredMixin,CreateView):
    model= Post
    form_class= PostForm
    template_name= 'add_post.html'
    #fields= '__all__'
    #fields= ('title','body')

class UpdatePostView(LoginRequiredMixin,UpdateView):
    model= Post
    form_class= UpdateForm
    template_name= 'update_post.html'
    #fields= ('title','title_tag','body')


class DeletePostView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url= reverse_lazy('home')


#def CategoryView(request, cats):
#    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
#    return render(request, 'categories.html', { 'cats':cats.title().replace('-', ' '), 'category_posts': category_posts })
    