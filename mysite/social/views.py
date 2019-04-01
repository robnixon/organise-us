from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.views import generic

from .forms import SignUpForm
from .models import Post, Org


class IndexView(generic.ListView):
    template_name = 'social/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the list of posts."""
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


class OrganisationView(generic.ListView):
    template_name = 'social/organisations.html'
    context_object_name = 'organisation_list'

    def get_queryset(self):
        """Return the list of organisations"""
        return Org.objects.all()


class DashboardView(generic.ListView):
    template_name = 'social/dashboard.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the list of posts."""
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'social/detail.html'


class PostCreate(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['post_text']

    def get_form(self, form_class=None):
        if self.request.user.is_authenticated:
            form = super(PostCreate, self).get_form(form_class)
            form.instance.user = self.request.user
            form.instance.organisation = self.request.user.orguser.organisation
            form.fields['post_text'].widget = forms.Textarea({'rows': 8, 'cols': 50})
            return form


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.orguser.image = form.cleaned_data.get('image')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('social:index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def update_org(request, org):
    org = get_object_or_404(Org, pk=org)
    if request.method == 'POST':
        request.user.orguser.organisation = org
        request.user.save()
    return redirect('social:index')
