from django.test import TestCase
from rest_framework.response import Response
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title="Banana Icecream", price=4.75, inventory=100)
        Menu.objects.create(title="Apple Juice", price=4.50, inventory=100)
        Menu.objects.create(title="Peach Juice", price=4.75, inventory=100)
        Menu.objects.create(title="Mango Juice", price=4.50, inventory=100)
        Menu.objects.create(title="Strawberry Juice", price=6.75, inventory=100)
        
    def test_getall(self):
        return dict(
            ins1 = Menu.objects.get(title='Banana Icecream'),
            ins2 = Menu.objects.get(title='Apple Juice'),
            ins3 = Menu.objects.get(title='Peach Juice'),
            ins4 = Menu.objects.get(title='Mango Juice'),
            ins5 = Menu.objects.get(title='Strawberry Juice'),
        )