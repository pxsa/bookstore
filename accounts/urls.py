
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpViews.as_view(), name='signup'),
]
