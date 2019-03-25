from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'social'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('new/', views.PostCreate.as_view(), name="new_post"),
    path('about', TemplateView.as_view(template_name='social/about.html'), name='about'),
    url(r'^accounts/login/$', LoginView.as_view(template_name='social/login.html'), name='login'),
    url(r'^accounts/logout/$', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
]
