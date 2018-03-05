from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import Http404
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
    if profile_type == 'individual':
        form = IndividualProfileForm(request.POST)
    elif profile_type == 'company':
        form = CompanyProfileForm(request.POST)
    else:
        raise Http404("what you do?")

    print(form)

    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect('home')
    return render(request, 'create_profile.html', {"form": form})
