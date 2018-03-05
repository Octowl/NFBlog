from django.contrib import admin

from .models import CompanyProfile, IndividualProfile

admin.site.register(CompanyProfile)
admin.site.register(IndividualProfile)
