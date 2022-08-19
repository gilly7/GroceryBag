from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            try:
                User.objects.get(username=username)
                messages.error(request, 'User already exists')
            except User.DoesNotExist:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Signup success')
                return redirect('signin')
        messages.error(request, "Username or Password is missing!")
    return render(request, 'signup.html')