from django.urls import path

from . import views

urlpatterns = [
    path('', views.PeopleView.as_view(), name="people"),
    path('add/', views.AddPerson.as_view(), name="add_person"),
    path('<slug>', views.PersonDetail.as_view(), name="person"),
    path('<person_slug>/update/', views.update_person, name="update_person"),
    path('<person_id>/delete/', views.delete_person, name="delete_person"),
    path('<person_slug>/like', views.like, name="like"),
]
