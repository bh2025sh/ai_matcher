from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

# First unregister the default one (if already registered)
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

# Now register your custom User with UserAdmin
@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Role info", {"fields": ("role",)}),
    )
    list_display = ("username", "email", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")

admin.site.register(CandidateProfile)

