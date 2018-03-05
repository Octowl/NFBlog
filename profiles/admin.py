from django.contrib import admin

from .models import Profile, CompanyProfile, IndividualProfile

admin.site.register(Profile)
admin.site.register(CompanyProfile)
admin.site.register(IndividualProfile)
