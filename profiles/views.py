from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import IndividualProfileForm, CompanyProfileForm


def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()

        password = form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=password)
        login(request, user)

        profile_type = request.POST.get('type')
        return redirect('create_profile', profile_type=profile_type)
    else:
        return render(request, 'signup.html', {
            "form": form,
        })


def create_profile(request, profile_type):
    if profile_type == 'I':
        form = IndividualProfileForm(request.POST)
    else:
        form = CompanyProfileForm(request.POST)

    print(form)

    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        print(profile)
        return redirect('home')
    return render(request, 'create_profile.html', {"form": form})
