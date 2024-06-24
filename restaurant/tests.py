from django.utils import timezone
from django.test import TestCase
from .models import MenuItem, Booking

# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.get_item(), "IceCream : 80")
        
class BookingTes(TestCase):
    def test_create_item(self):
        item = Booking(
            name = "Amanda",
            no_of_guests = 5,
            booking_date = timezone.now().date()
        )
        item.save()
        
        expected_string = f"Booking 1 in Amanda's name for 5 people on {timezone.now().date()}"
        
        self.assertEqual(item.__str__(), expected_string)