from django.shortcuts import render, get_object_or_404
from .models import Person, Team


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


def person(request, person_id):
    _person = get_object_or_404(Person, id=person_id)
    return render(request,
                  "person.html",
                  context={"person": _person})


def team(request, team_id):
    _team = get_object_or_404(Team, id=team_id)
    return render(request,
                  "team.html",
                  context={"team": _team})
