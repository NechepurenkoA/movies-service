from django.contrib import admin

from profiles.models import Profile


class ProfileInLine(admin.TabularInline):
    """Directors / Movies admin panel inline"""

    model = Profile
    extra = 1
