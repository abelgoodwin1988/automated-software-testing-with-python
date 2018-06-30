from unittest import TestCase
from models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('test', 19.99)

        self.assertIsNotNone(item)
        self.assertEqual(item.name, 'test',
                         "Name after item creation does not equal constructor argument")
        self.assertEqual(item.price, 19.99,
                         "Price after item creation does not equal constructor argument")

    def test_item_json(self):
        item = ItemModel('test', 19.99)

        expected = {'name': 'test', 'price': 19.99}

        self.assertEqual(item.json(), expected)

    def test_find_by_name(self):
        pass

    def test_save_to_db(self):
        pass

    def test_delete_from_db(self):
        pass
