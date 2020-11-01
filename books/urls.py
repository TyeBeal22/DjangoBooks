from django.urls import path
from .views import (
    book_list, 
    book_detail, 
    chapter_detail,
    exercise_detail,
    ebooks
)

app_name = 'books'

urlpatterns = [
    path('', book_list, name='book-list'),
    path('<slug>/', book_detail, name='book-detail'),
    path('<book_slug>/<int:chapter_number>', chapter_detail, name='chapter-detail'),
    path('<book_slug>/<int:chapter_number>/<int:exercise_number>/', exercise_detail, name='exercise-detail'),
    path('ebooks/', ebooks, name='exercise-detail'),
    path('ebook/<int:ebook_id>', ebooks, name='exercise-detail')
]