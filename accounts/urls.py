from django.urls import path

from . import views

urlpatterns = [
    path('singup/', views.CreatUser.as_view() , name='signup'),
]