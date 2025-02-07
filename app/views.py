from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomLoginForm, SignupForm  # ✅ Ensure this line is correct
from django.contrib import messages  # ✅ Import Django's messages framework

# ✅ Login View
def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! You have successfully logged in.")  # ✅ Message added

            return redirect('home')  # Redirect to home page
    else:
        form = CustomLoginForm()
    return render(request, 'app/login.html', {'form': form})

# ✅ Logout View
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# ✅ Signup View
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after signup
            return redirect('home')  # Redirect to home after successful signup
    else:
        form = SignupForm()

    return render(request, 'app/signup.html', {'form': form})

# ✅ Home View
def home_view(request):
    return render(request, 'app/home.html')
