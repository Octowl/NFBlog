from django.shortcuts import render, redirect, get_object_or_404

from .models import Person, Team
from .forms import PersonForm


def home(request):
    special_people = Person.objects.all().filter(is_special=True)
    return render(request,
                  "home.html",
                  context={"people": special_people})


def people(request):
    people_list = Person.objects.all()
    return render(request,
                  "people.html",
                  context={"people": people_list})


def person(request, person_slug):
    _person = get_object_or_404(Person, slug=person_slug)
    context = {}
    context["person"] = _person
    context["person_teams"] = _person.teams.all()
    return render(request,
                  "person.html",
                  context=context)


def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            new_person = form.save()
            return redirect(new_person)
    form = PersonForm()
    context = {"form": form}
    return render(request, "add_person.html", context)


def team(request, team_slug):
    _team = get_object_or_404(Team, slug=team_slug)

    context = {}
    context["team"] = _team
    context["members"] = _team.members.all()
    return render(request,
                  "team.html",
                  context=context)
