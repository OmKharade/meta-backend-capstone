from django.test import TestCase
from restaurant.models import Booking, Menu
from datetime import date

class BookingModelTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(name="John Doe", no_of_guests=4, booking_date=date.today())

    def test_string_representation(self):
        self.assertEqual(str(self.booking), f"{self.booking.name}, {self.booking.no_of_guests} guests on {self.booking.booking_date}")

    def test_booking_fields(self):
        self.assertEqual(self.booking.name, "John Doe")
        self.assertEqual(self.booking.no_of_guests, 4)
        self.assertTrue(isinstance(self.booking.booking_date, date))

class MenuModelTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_string_representation(self):
        self.assertEqual(str(self.menu_item), "IceCream : 80")

    def test_menu_fields(self):
        self.assertEqual(self.menu_item.title, "IceCream")
        self.assertEqual(self.menu_item.price, 80)
        self.assertEqual(self.menu_item.inventory, 100)

    def test_price_field(self):
        self.menu_item.price = 150.50
        self.menu_item.save()
        self.assertEqual(Menu.objects.get(id=self.menu_item.id).price, 150.50)

    def test_inventory_update(self):
        self.menu_item.inventory -= 1
        self.menu_item.save()
        self.assertEqual(Menu.objects.get(id=self.menu_item.id).inventory, 99)
        self.assertEqual(Menu.objects.get(id=self.menu_item.id).inventory, 99)