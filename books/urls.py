from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='books'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book'),
    path('create/', views.BookCreateView.as_view(), name='book_create'),
    path('update/<int:pk>/', views.BookUpdateView.as_view(), name='book_update'),
    path('delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),
]