from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from django.contrib.auth import get_user_model
from datetime import date, timedelta

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample listings, bookings, and reviews.'

    def handle(self, *args, **kwargs):
        # Create sample users
        user1, _ = User.objects.get_or_create(username='user1', defaults={'email': 'user1@example.com'})
        user2, _ = User.objects.get_or_create(username='user2', defaults={'email': 'user2@example.com'})

        # Create sample listings
        listing1 = Listing.objects.create(title='Beach House', description='A lovely house by the beach.', location='Miami', price=250.00)
        listing2 = Listing.objects.create(title='Mountain Cabin', description='Cozy cabin in the mountains.', location='Aspen', price=180.00)

        # Create sample bookings
        Booking.objects.create(listing=listing1, user=user1, start_date=date.today(), end_date=date.today()+timedelta(days=3), status='confirmed')
        Booking.objects.create(listing=listing2, user=user2, start_date=date.today()+timedelta(days=5), end_date=date.today()+timedelta(days=10), status='pending')

        # Create sample reviews
        Review.objects.create(listing=listing1, user=user2, rating=5, comment='Amazing stay!')
        Review.objects.create(listing=listing2, user=user1, rating=4, comment='Very comfortable.')

        self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))
