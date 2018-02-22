from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    is_special = models.BooleanField(default=False)
    team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.SET_NULL, related_name="members")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
