from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profile

@login_required
def follow(request, username):
    user = get_object_or_404(User, username=username)
    if request.user.profile.is_following(user):
        return JsonResponse({'error': f'You are already following {user.username}'})
    if request.user == user:
        return JsonResponse({'error': 'You cannot follow yourself'})
    request.user.profile.follow(user)
    request.user.profile.save()
    return JsonResponse({
        'btnLabel': 'Unfollow',
        'count': user.followers.count(),
        'url': reverse('unfollow', kwargs={'username':user.username})
    })

@login_required
def unfollow(request, username):
    user = get_object_or_404(User, username=username)
    if not request.user.profile.is_following(user):
        return JsonResponse({'error': f'You are not following {user.username}'})
    if request.user == user:
        return JsonResponse({'error': 'You cannot unfollow yourself'})
    request.user.profile.unfollow(user)
    request.user.profile.save()
    return JsonResponse({
        'btnLabel': 'Follow',
        'count': user.followers.count(),
        'url': reverse('follow', kwargs={'username':user.username})
    })