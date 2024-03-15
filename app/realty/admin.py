from django.contrib import admin

from .models import Flat, Floor, Section, Building

admin.site.register(Flat)
admin.site.register(Floor)
admin.site.register(Section)
admin.site.register(Building)
