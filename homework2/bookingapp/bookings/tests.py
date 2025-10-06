from django.test import TestCase
from .models import Movie, Seat, Booking
from django.contrib.auth.models import User

# Create your tests here.
class MovieModelTest(TestCase):
    def testMovie(self):
        movie = Movie.objects.create(
            title="Inception",
            description="Mind-bending thriller",
            release_date="2010-07-16",
            duration=148
        )
        self.assertEqual(movie.title, "Inception")
        self.assertEqual(str(movie), "Inception")

class SeatModelTest(TestCase):
    def testSeat(self):
        seat = Seat.objects.create(seat_number="A1", is_booked=False)
        self.assertFalse(seat.is_booked)

class BookingModelTest(TestCase):
    def testBooking(self):
        user = User.objects.create(username="testuser")
        movie = Movie.objects.create(
            title="Matrix",
            description="Sci-fi classic",
            release_date="1999-03-31",
            duration=136
        )
        seat = Seat.objects.create(seat_number="B2", is_booked=False)
        booking = Booking.objects.create(user=user, movie=movie, seat=seat)
        self.assertEqual(booking.user.username, "testuser")