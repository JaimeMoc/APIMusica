from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Profile, ProfileType

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'date_joined')
    date_hierarchy = 'date_joined'
    ordering = ('-id')
    
    fieldsets = (
        ( None, {
               "fields": ('username', 'password')
            }
        ),
        (
            ("User Info"), {
                'fields':('first_name', 'last_name', 'email')
            }
        ),
        (   ("Metadata"), {
                'fields': ('last_login', 'date_joined')
            }
        ),
    )

class ProfileTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile_type')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile_type')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ProfileType, ProfileTypeAdmin)
admin.site.register(Profile, ProfileAdmin) 