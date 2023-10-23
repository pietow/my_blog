from django import forms
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Post

# Create your views here.
class BlogForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Post
        fields = ['title', 'body', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    
class BlogCreateView(CreateView): # new
    model = Post
    template_name = "post_new.html"
    # fields = ['title', 'author', 'body']
    form_class = BlogForm

    # def get_success_url(self):
    #     return reverse('post_detail', kwargs={'pk': self.object.pk})

class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = "post_edit.html"
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    # template_name = "post_delete.html"
    success_url = reverse_lazy("home")
    

