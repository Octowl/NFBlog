from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
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
    teams = models.ManyToManyField(Team, related_name="members")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_profile_picture(self):
        if self.profile_picture and hasattr(self.profile_picture, 'url'):
            return self.profile_picture.url
        return 'https://www.fillmurray.com/200/300'

    class Meta:
        ordering = ['name']


def create_slug(instance, Model, field, new_slug=None):
    slug = new_slug or slugify(getattr(instance, field))
    qs = Model.objects.filter(slug=slug).order_by('-id')
    if qs.exists():
        new_slug = f'{slug}-{instance.id}'
        create_slug(instance, Model, field, new_slug=new_slug)
        return slug

@receiver(pre_save, sender=Person)
def add_slug_to_person(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance, Person, 'name')
