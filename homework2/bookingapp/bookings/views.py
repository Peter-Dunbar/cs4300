from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    def perform_update(self, serializer):
        serializer.save(is_booked=True)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})


@login_required
def seat_booking(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    seats = Seat.objects.all()
    if request.method == "POST":
        seat_id = request.POST.get("seat_id")
        seat = Seat.objects.get(id=seat_id)
        if not seat.is_booked:
            seat.is_booked = True
            seat.save()
            Booking.objects.create(movie=movie, seat=seat, user=request.user)
            return redirect("booking_history")
    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})


@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})
