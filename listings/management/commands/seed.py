from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **options):
        sample_listings = [
            {
                "title": "Beachfront Apartment",
                "description": "A beautiful apartment overlooking the ocean.",
                "price_per_night": 150.00,
                "location": "Cape Town"
            },
            {
                "title": "Safari Lodge",
                "description": "Experience wildlife up close with comfort.",
                "price_per_night": 220.00,
                "location": "Kruger National Park"
            },
            {
                "title": "City Center Studio",
                "description": "Perfect for business travelers.",
                "price_per_night": 90.00,
                "location": "Johannesburg"
            }
        ]

        for data in sample_listings:
            Listing.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
