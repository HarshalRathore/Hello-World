from django.contrib import admin
from authentication.models import Profile
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin


class ProfileAdmin(UserAdmin, ImportExportModelAdmin):
    search_fields = ('email', 'phone_number', 'user_id')
    ordering = ('email',)
    list_display = ('email', 'phone_number', 'user_id', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'user_id', 'password', 'otp')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    readonly_fields = ('user_id',)

admin.site.register(Profile, ProfileAdmin)