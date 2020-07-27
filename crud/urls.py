from django.urls import path, include
from .views import book_api_view, book_api_update_view, BookList, BookDetail


urlpatterns = [
    path('', book_api_view, name='book'),
    path('class/', BookList.as_view(), name='bookc'),
    path('class/<int:pk>', BookDetail.as_view(), name='bookdc'),
    # path('details/<int:pk>', UserDetail.as_view(), name='update'),
    path('auth', include('rest_framework.urls')),
]
