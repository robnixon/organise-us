from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name = 'social'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('post/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('posts/new/', views.PostCreate.as_view(), name="new_post"),
    path('about', TemplateView.as_view(template_name='social/about.html'), name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.signup, name='signup'),
]
