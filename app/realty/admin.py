from django.contrib import admin

from realty.models import Flat
from realty.models import Floor
from realty.models import Section
from realty.models import Building
from realty.models import Project


admin.site.register(Flat)
admin.site.register(Floor)
admin.site.register(Section)
admin.site.register(Building)
admin.site.register(Project)
