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
    path('resetpwd/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password-reset'),
    path('resetpwd/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('resetpwd/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('resetpwd/success/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
]