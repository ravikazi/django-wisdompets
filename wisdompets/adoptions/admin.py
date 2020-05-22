from django.contrib import admin

from .models import Pet

@admin.register(Pet)

class PetAdmin(admin.ModelAdmin):
	#pass
	list_display = ['name','species','breed','age','sex']
	