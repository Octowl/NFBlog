from django.shortcuts import render, get_object_or_404
from .models import Person, Team


def get_all_teams():
    return Team.objects.all()


def context_with_teams(context):
    context["teams"] = get_all_teams()
    return context


def home(request):
    special_people = Person.objects.all().filter(is_special=True)
    context = context_with_teams({"people": special_people})
    return render(request,
                  "home.html",
                  context=context)


def people(request):
    people_list = Person.objects.all()
    context = context_with_teams({"people": people_list})
    return render(request,
                  "people.html",
                  context=context)


def person(request, person_id):
    _person = get_object_or_404(Person, id=person_id)
    context = context_with_teams({"person": _person})
    return render(request,
                  "person.html",
                  context=context)


def team(request, team_id):
    _team = get_object_or_404(Team, id=team_id)
    context = context_with_teams({"team": _team})
    return render(request,
                  "team.html",
                  context=context)
