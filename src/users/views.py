from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from main.views import home_view
from django.contrib.auth.forms import UserCreationForm
from django.views import View

def register_view(request):
    form = UserCreationForm()
    return render(request, "views/register.html", {"registration_form": form})

def login_view(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('home')  # Assuming 'home' is the name of your home URL pattern
            else:
                messages.error(request, "Invalid credentials.")
                return render(request, "views/login.html", {"login_form": login_form})
        else:
            # Form is not valid, re-render with errors
            messages.error(request, "Invalid credentials.")
            return render(request, "views/login.html", {"login_form": login_form})
    else:
        # GET or any other method
        login_form = AuthenticationForm()
        return render(request, "views/login.html", {"login_form": login_form})
    

def register_view(request):
    form = UserCreationForm()
    #return HttpResponse("Register View")  # Placeholder for the register view
    return render(request, "views/register.html", {"registration_form": form})

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "views/register.html", {"registration_form": form})

    def post(self, request):
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()  # Ensure the user instance is updated
            messages.success(request, "Registration successful!")
            return redirect('login')  # Redirect to login after successful registration
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
            return render(request, "views/register.html", {"registration_form": register_form})    