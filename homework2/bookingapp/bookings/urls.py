from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list, name="movie_list"),
    path('movies/<int:movie_id>/book/', views.seat_booking, name="seat_booking"),
    path('history/', views.booking_history, name="booking_history"),
]