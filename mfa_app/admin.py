# your_app/admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

# Customizing the User admin interface
class CustomUserAdmin(UserAdmin):
    # Specify which fields should appear in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    
    # Add search functionality
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    # Add filters to the list view
    list_filter = ('is_active', 'is_staff')
    
    # Organize the form fields into groups
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
    # Add additional fields to the "add" user form (e.g., `is_active`, `is_staff`)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )

# Register the custom UserAdmin
admin.site.unregister(User)  # Unregister the original User model
admin.site.register(User, CustomUserAdmin)  # Register the custom UserAdmin

# Register the UserProfile model with the admin interface
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_mfa_enabled', 'is_mfa_verified', 'otp_secret')
    search_fields = ('user__username', 'user__email')
    list_filter = ('is_mfa_enabled', 'is_mfa_verified')
    fieldsets = (
        (None, {
            'fields': ('user', 'otp_secret', 'is_mfa_enabled', 'is_mfa_verified')
        }),
    )

admin.site.register(UserProfile, UserProfileAdmin)
