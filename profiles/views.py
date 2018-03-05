from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import ProfileForm


def signup(request):
    user_form = UserCreationForm(request.POST)
    profile_form = ProfileForm(request.POST)
    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()

        password = user_form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=password)
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'signup.html', {
            "user_form": user_form,
            "profile_form": profile_form
        })
