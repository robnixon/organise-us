from django.forms import forms
from django.utils import timezone
from django.views import generic
from .models import Post


class IndexView(generic.ListView):
    template_name = 'social/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the list of posts."""
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'social/detail.html'


class PostCreate(generic.CreateView):
    model = Post
    fields = ['post_text', 'user']

    class Meta:
        model = Post
        widgets = {
            'post_text': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }
