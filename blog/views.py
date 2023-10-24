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
    

    
from django.views import View
from django.http import HttpResponse

class SessionExampleView(View):
    
    def get(self, request, *args, **kwargs):
        # Check if session_key is already set
        print(request.user.is_authenticated)
        print(request.META)
        if request.session.session_key:
            response_text = f"Welcome back! Your session key is: {request.session.session_key}"
        else:
            # Django automatically creates a session_key when session data is set
            request.session['example_data'] = 'This is some session data.'
            response_text = "Welcome! Your session has been initialized and you've been given a session key."

        return HttpResponse(response_text)

