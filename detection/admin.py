from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Customize the UserAdmin to remove 'groups'
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    ]

    # Remove 'groups' from the add user form as well
    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    ]

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'is_superuser')


# Unregister the default UserAdmin
admin.site.unregister(User)

# Register the customized UserAdmin without 'groups'
admin.site.register(User, CustomUserAdmin)
