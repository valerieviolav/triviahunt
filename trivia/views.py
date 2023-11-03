from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# Create your views here.
from django.http import HttpResponse

@login_required
def index(request):
    return render(request, "trivia/index.html")

def create_username(request):
    # Check if the user already has a profile
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()

    if request.method == 'POST':
        # Handle form submission to update the username
        # You can use Django forms for this
        pass
    return render(request, 'create_username.html', {'profile': profile})