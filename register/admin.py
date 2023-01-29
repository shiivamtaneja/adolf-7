from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UAdmin
from .models import User

# Register your models here.
class UserAdmin(UAdmin):
    model = User
    list_display = ('phone_number', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('phone_number', 'first_name', 'last_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('phone_number', 'first_name', 'last_name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_adolf_staff', 'is_distributer', 'is_retailer', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('phone_number',)
    ordering = ('phone_number',)
admin.site.register(User, UserAdmin)