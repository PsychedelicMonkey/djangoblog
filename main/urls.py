from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/create/', views.PostCreateView.as_view(), name='create-post'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]