from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_civil_id(civil_id):
    if len(str(civil_id)) != 12:
        raise ValidationError(
            _('%(civil_id)s is not twelve digits'),
            params={'civil_id': civil_id}
        )


class IndividualProfile(models.Model):

    GENDER_CHOICES = (
        ("M", "male"),
        ("F", "female")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    civil_id = models.PositiveIntegerField(validators=[validate_civil_id])
    gender = models.CharField(blank=True, max_length=1, choices=GENDER_CHOICES)
    website = models.URLField(blank=True)


class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField()
    location_url = models.URLField()
