# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User

# Registration view (for user signup)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Get the username from the form
            username = form.cleaned_data.get('username')
            
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, f"Username '{username}' is already taken. Please choose another.")
                return redirect('register')  # Redirect back to the registration page

            # If the username is unique, save the user to the database
            form.save()
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    
    return render(request, 'games/register.html', {'form': form})
# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in
            return redirect('login')  # Redirect to home page after login
    else:
        form = AuthenticationForm()

    return render(request, 'games/login.html', {'form': form})

def about(request):
    return render(request, 'games/about.html')


# Logout view
@csrf_protect
def logout_view(request):
    logout(request)  # Log the user out
    return redirect('about')  # Redirect to the home page after logout

# Home page (accessible by everyone)
def home(request):
    return render(request, 'games/home.html')  # Display game selection page

def play(request):
    return render(request, 'games/dashgame.html')
