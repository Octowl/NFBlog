from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.db.models import Q

from .models import Person, Team
from .forms import PersonForm


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def test(request):
    print("POST:\n")
    print(request.POST or "lol")
    print("\nGET:\n")
    print(request.GET)
    return render(request, 'test.html', {"post": request.POST, "get": request.GET})


def home(request):
    special_people = Person.objects.all().filter(is_special=True)
    return render(request,
                  "home.html",
                  context={"people": special_people})


def people(request):
    people_list = Person.objects.all()
    query = request.GET.get('search')
    if query:
        people_list = people_list.filter(Q(name__icontains=query) | Q(bio__icontains=query)).distinct()

    return render(request,
                  "people.html",
                  context={"people": people_list})


def person(request, person_slug):
    _person = get_object_or_404(Person, slug=person_slug)
    context = {}
    context["person"] = _person
    context["person_teams"] = _person.teams.all()
    context["is_liked"] = request.user in _person.liked_by.all()
    return render(request,
                  "person.html",
                  context=context)


def add_person(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    form = PersonForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            new_person = form.save(commit=False)
            new_person.creator = request.user
            new_person.save()
            return redirect(reverse('person', args=[new_person.slug]))
    else:
        context = {"form": form}
        return render(request, "add_person.html", context)


def update_person(request, person_slug):
    person = Person.objects.get(slug=person_slug)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect(person)
    else:
        form = PersonForm(instance=person)
        context = {
            "person": person,
            "form": form
        }
        return render(request, "update_person.html", context)


def like(request, person_slug):
    person = get_object_or_404(Person, slug=person_slug)
    if request.user not in person.liked_by.all():
        person.liked_by.add(request.user)
    else:
        person.liked_by.remove(request.user)
    return JsonResponse({'like_count': person.likes})


def delete_person(request, person_id):
    Person.objects.get(id=person_id).delete()
    return redirect("people")


def team(request, team_slug):
    _team = get_object_or_404(Team, slug=team_slug)

    context = {}
    context["team"] = _team
    context["members"] = _team.members.all()
    return render(request,
                  "team.html",
                  context=context)
