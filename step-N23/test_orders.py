import unittest
from orders import process_orders




class TestProcessOrders(unittest.TestCase):

    def test_product_not_in_inventory(self):
        orders = [{"product": "banana", "quantity": 5}]
        inventory = {"apple": 10}

        with self.assertRaises(ValueError):
            process_orders(orders, inventory)

    def test_not_enough_quantity(self):
        orders = [{"product": "apple", "quantity": 20}]
        inventory = {"apple": 10}

        with self.assertRaises(ValueError):
            process_orders(orders, inventory)

    def test_successful_order(self):
        orders = [{"product": "apple", "quantity": 5}]
        inventory = {"apple": 10}

        result = process_orders(orders, inventory)

        self.assertEqual(result, orders)

        self.assertEqual(inventory["apple"], 5)




if __name__ == "__main__":
    unittest.main()