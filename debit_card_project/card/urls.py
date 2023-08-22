from django.urls import path
from .views import CardList, CardDetail

urlpatterns = [
    path('card/', CardList.as_view(), name='card-list'),
    path('card/<int:pk>/', CardDetail.as_view(), name='card-detail'),
]