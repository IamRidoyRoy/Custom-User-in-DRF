from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    # Add these lines for search functionality
    search_fields = ('username', 'email')


admin.site.register(CustomUser, CustomUserAdmin)
