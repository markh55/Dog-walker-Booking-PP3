from django.urls import path
from .views import WalkListView, BookingCreateView, ReviewCreateView

urlpatterns = [
    path('', WalkListView.as_view(), name='walk-list'),
    path('create-booking/', BookingCreateView.as_view(), name='booking-create'),
    path('create-review/', ReviewCreateView.as_view(), name='review-create'),
]
