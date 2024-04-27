from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomeUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomeUser
        fields = UserCreationForm.Meta.fields + ('age',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomeUser
        fields = UserChangeForm.Meta.fields  