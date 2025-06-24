from django.urls import path
from . import views

urlpatterns = [
# path('', views.WalkListView.as_view(), name='walk-list'),
    path('', views.booking_list, name='booking-list'),
    path('create-booking/', views.BookingCreateView.as_view(), name='booking-create'),
]