from django.urls import path

from . import views

urlpatterns = [
    path('', views.people, name="people"),
    path('<int:person_id>', views.person, name="person"),
    path('teams/<int:team_id>', views.team, name="team"),
]
