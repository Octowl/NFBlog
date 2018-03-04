from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.urls import reverse

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User

from django.db import models

import random


class Team(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    is_special = models.BooleanField(default=False)
    teams = models.ManyToManyField(Team, related_name="members", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('person', args=[self.slug])

    def get_profile_picture(self):
        if self.profile_picture and hasattr(self.profile_picture, 'url'):
            return self.profile_picture.url
        return 'https://www.fillmurray.com/200/300'

    class Meta:
        ordering = ['name']


def validate_civil_id(civil_id):
    if len(str(civil_id)) != 12:
        raise ValidationError(
            _('%(civil_id)s is not twelve digits'),
            params={'civil_id': civil_id}
        )


class Profile(models.Model):

    GENDER_CHOICES = (
        ("M", "male"),
        ("F", "female")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    civil_id = models.PositiveIntegerField(validators=[validate_civil_id])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


def create_slug(instance, Model, field_name, new_slug=None):
    slug = new_slug or slugify(getattr(instance, field_name), allow_unicode=True)
    qs = Model.objects.filter(slug=slug).order_by('-id')
    if qs.exists():
        new_slug = f'{slug}-{qs.first().id}'
        return create_slug(instance, Model, field_name, new_slug=new_slug)
    return slug


@receiver(pre_save, sender=Person)
def add_slug_to_person(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance, sender, 'name')


@receiver(pre_save, sender=Team)
def add_slug_to_team(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance, sender, 'name')
