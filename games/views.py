# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from .forms import UserUpdateForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import CombinedUserForm, CustomUserCreationForm

# Registration view (for user signup)
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Use the custom form
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            # Check if the email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, f"Email '{email}' is already in use. Please choose another.")
                return redirect('register')  # Redirect if email exists

            # Save the user to the database
            form.save()
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')  # Redirect after successful registration
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()  # For GET requests, display the empty form

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

@login_required
def user_settings(request):
    if request.method == 'POST':
        form = CombinedUserForm(request.user, request.POST)
        if form.is_valid():
            # Save user details
            form.save()

            # Update session hash to keep the user logged in after password change
            update_session_auth_hash(request, form.user)

            messages.success(request, "Your profile and password have been updated successfully.")
            return redirect('user_settings')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CombinedUserForm(request.user)

    return render(request, 'games/user_settings.html', {'form': form})