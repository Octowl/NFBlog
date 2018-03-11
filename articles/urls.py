from django.urls import path

from . import views

urlpatterns = [
    path('', views.people, name="people"),
    path('add_person/', views.add_person, name="add_person"),
    path('update_person/<person_slug>', views.update_person, name="update_person"),
    path('delete_person/<person_id>', views.delete_person, name="delete_person"),
    path('<person_slug>', views.person, name="person"),
    path('<person_slug>/like', views.like, name="like"),
]
