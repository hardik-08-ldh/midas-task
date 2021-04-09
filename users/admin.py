from django.contrib import admin

# Register models on admin site.
from .models import Profile

admin.site.register(Profile)