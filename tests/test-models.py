from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Mango Icecream", price=4.50, inventory=100)
        self.assertEqual(item, "Mango Icecream : 4.50")