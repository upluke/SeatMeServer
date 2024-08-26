from django.urls import path 
from .views import get_bookings, create_booking, booking_detail

urlpatterns = [
    path('bookings/', get_bookings, name = 'get_bookings'),
    path('bookings/create/', create_booking, name='create_booking'),
    path('bookings/<int:pk>', booking_detail, name='booking_detail')
]
