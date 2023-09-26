from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Map the root URL to the index view
    path('authors/<str:author>/', views.books, name='books'),  # Map URLs like 'authors/anidruth/' to the books view
    path('redirect_to_books/<str:author_name>/', views.redirect_to_books, name='redirect_to_books'),
    path('add_book/', views.add_book, name='add_book'),  # For adding books without specifying the author
    # path('add_book/<str:author_name>/', views.add_book, name='add_book_with_author'),  # For adding books with an author
    path('search/', views.search_book, name='search_book'),
    path('delete_author/<str:author>', views.delete_author, name='delete_author')
]
