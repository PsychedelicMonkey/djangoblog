from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import followers

urlpatterns = [
    path('follow/<str:username>/', followers.follow, name='follow'),
    path('unfollow/<str:username>/', followers.unfollow, name='unfollow'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/edit/', views.edit_profile, name='edit-profile'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html', extra_context={'title': 'Log In'}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html', extra_context={'title': 'Log In'}), name='logout'),
]