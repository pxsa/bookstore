from django.urls import path

from .views import CreatUser


urlpatterns = [
    path('signup/', CreatUser.as_view(), name='signup'),
]