from section5.models.item import ItemModel
from section5.tests.basetest import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99)

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))
