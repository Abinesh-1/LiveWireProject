from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse


# Home page view
def index(request):
    return render(request, "index.html")

# About page view
def about(request):
    return render(request, "about.html")

# Redirect old URL to new URL
def oldurl(request):
    return redirect(reverse("livewire:newurl"))

# New URL view
def newurl(request):
    return HttpResponse("This is the new URL")

# Sign in view
def signin(request):
    if request.method == 'POST':
        username = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("livewire:index")
        else:
            messages.error(request, "Invalid User or Password")
            return redirect("livewire:signin")
    return render(request, 'signin.html')

# Sign up view
def signup(request):
    if request.method == 'POST':
        username = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("livewire:signup")

        if password != confirmpassword:
            messages.error(request, "Password does not match")
            return redirect("livewire:signup")

        # Create the user
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request, "Signup successful! Go to login...")
        return redirect("livewire:signin")  # Redirect to signin after successful signup
    
    return render(request, 'signup.html')

# Sign out view
def signout(request):
    logout(request)
    return redirect("livewire:index")


@login_required
def enroll(request):
    print("hmm")
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        course = request.POST.get("course")

        subject = "Thank you for registering!"
        
        message = render_to_string("Thankyoumail.html", {
            "name": name,
            "course": course
        })

        send_mail(
            subject,
            message,
            'no-reply@example.com',  
            [email],        
            fail_silently=False
        )

        messages.success(request, "Enrollment successful! Check your email.")
        return redirect("livewire:index")  

    return render(request, "enrollform.html") 


def api_users(request):
    users = User.objects.all().values('id', 'username', 'email', 'date_joined')
    users_list = list(users)
    return JsonResponse({'users': users_list}, safe=False)