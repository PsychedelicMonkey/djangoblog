from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/create/', views.PostCreateView.as_view(), name='create-post'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(template_name='main/edit_post.html'), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]