from django.contrib import admin

from realty.models.flat import Flat
from realty.models.floor import Floor
from realty.models.section import Section
from realty.models.building import Building
from realty.models.project import Project


admin.site.register(Flat)
admin.site.register(Floor)
admin.site.register(Section)
admin.site.register(Building)
admin.site.register(Project)
