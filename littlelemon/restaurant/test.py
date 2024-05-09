from django.test import TestCase
from restaurant.models import Menu
from .serializers import MenuSerializer

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Salad", price=50, inventory=30)
        Menu.objects.create(title="Cake", price=60, inventory=20)

    def test_getall(self):
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        expected_result = [
            {'title': 'Salad', 'price': '50.00', 'inventory': '30.00'}, 
            {'title': 'Cake', 'price': '60.00', 'inventory': '20.00'}
        ]
        self.assertEqual(serialized_items.data, expected_result)

       
       