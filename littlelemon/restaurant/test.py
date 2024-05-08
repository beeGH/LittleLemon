from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Salad", price=50, inventory=30)
        Menu.objects.create(title="Cake", price=60, inventory=20)

        def test_getall(self):
            