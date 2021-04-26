from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, EditUserForm, EditProfileForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is created!')
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'title': 'Sign Up',
        'form': form,
    }
    return render(request, 'user/register.html', context)

def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.post_set.order_by('-created')
    context = {
        'user': user,
        'posts': posts,
    }
    return render(request, 'user/profile.html', context)

@login_required
def edit_profile(request, username):
    if request.method == 'POST':
        u_form = EditUserForm(request.POST, instance=request.user)
        p_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile is updated')
            return redirect('profile', request.user.username)
    else:
        u_form = EditUserForm(instance=request.user)
        p_form = EditProfileForm(instance=request.user.profile)
    context = {
        'title': 'Edit Your Profile',
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'user/edit_profile.html', context)