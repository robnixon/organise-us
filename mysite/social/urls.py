from django.urls import path
from . import views

app_name = 'social'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('new/', views.PostCreate.as_view(), name="new_post"),
]
