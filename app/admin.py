from django.contrib import admin
from .models import Profile, Blog

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'gender', 'date', 'updated']

class BlogAdmin(admin.ModelAdmin):
	list_display = ['user', 'title', 'rate', 'updated']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Blog, BlogAdmin)
