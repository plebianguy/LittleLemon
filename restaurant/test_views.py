from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from decimal import Decimal
from datetime import datetime

class MenuViewTest(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.menu_item_1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.menu_item_2 = MenuItem.objects.create(title="Cake", price=150, inventory=50)
        self.menu_item_3 = MenuItem.objects.create(title="Pie", price=60, inventory=30)
        self.url = reverse('menu')

    def test_get_all_menu_items(self):
        response = self.client.get(self.url)
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_menu_item(self):
        data = {
            'title': "Burger",
            'price': '50.00',
            'inventory': 20
        }
        response = self.client.post(self.url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['price'], data['price'])
        self.assertEqual(response.data['inventory'], data['inventory'])

        # Verify that the item was actually created in the database
        created_item = MenuItem.objects.get(title="Burger")
        self.assertEqual(created_item.price, Decimal(data['price']))
        self.assertEqual(created_item.inventory, data['inventory'])
        
class BookingViewTest(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.booking1 = Booking.objects.create(name = "David",no_of_guests = 3, booking_date = datetime(year = 2024, month= 6, day = 25))
        self.booking2 = Booking.objects.create(name = "Roger",no_of_guests = 4, booking_date = datetime(year = 2024, month= 6, day = 26))
        self.booking3 = Booking.objects.create(name = "Richard",no_of_guests = 2, booking_date = datetime(year = 2024, month= 6, day = 25))
        self.booking1 = Booking.objects.create(name = "Nick",no_of_guests = 5, booking_date = datetime(year = 2024, month= 6, day = 25))
        self.url = reverse("tables-list")
        
    def test_get_all_bookings(self):
        response = self.client.get(self.url)
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many = True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
    def test_create_booking(self):
        data = {
            'name': "Syd",
            'no_of_guests': 1,
            "booking_date" : "2024-06-30T00:00:00Z"
        }
        response = self.client.post(self.url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['no_of_guests'], data['no_of_guests'])
        self.assertEqual(response.data['booking_date'], data['booking_date'])

