# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomerUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('mometary', 'type_user',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('mometary', 'type_user',)}),
    )

admin.site.register(CustomerUser, CustomUserAdmin)
