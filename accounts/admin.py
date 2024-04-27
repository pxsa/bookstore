from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomeUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomeUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    # for adding extra adj to ui
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )

    list_display = ['username', 'email', 'age', 'is_staff']


admin.site.register(CustomeUser, CustomUserAdmin)
