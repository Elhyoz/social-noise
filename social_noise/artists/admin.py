from django.contrib import admin
from .models import Artist


class AdminArtist(admin.ModelAdmin):
	list_display = ["__str__", "name"]
	list_display_links = ["email"]
	list_filter = ["name"]
	list_editable = ["email", "name"]

		
admin.site.register(Artist)
