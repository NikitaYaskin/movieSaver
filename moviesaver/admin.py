from django.contrib import admin
from .models import Movie, Status, Section

admin.site.register(Section)
admin.site.register(Status)
admin.site.register(Movie)