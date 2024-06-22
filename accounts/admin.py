from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )
    list_display = ['username', 'email', 'age', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)
