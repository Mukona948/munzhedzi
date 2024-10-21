from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login  # For logging in user after registration

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hello {username}, your account has been created! Please log in.')
            # You can automatically log in the user if needed:
            # auth_login(request, user)
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')  # Redirect to login page after logging out

@login_required
def profile_page(request):
    return render(request, 'users/profile.html')
