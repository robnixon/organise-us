from django import forms
from django.shortcuts import redirect
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
    fields = ['post_text']

    def get_form(self, form_class=None):
        form = super(PostCreate, self).get_form(form_class)
        form.instance.user = self.request.user
        form.fields['post_text'].widget = forms.Textarea()
        return form

def redirect_view(request):
    response = redirect('social/index')
    return response