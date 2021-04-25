from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

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
