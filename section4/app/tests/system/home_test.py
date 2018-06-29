from section4.app.tests.system.basetest import BaseTest
import json

class TestHome(TestCase):
    def test_home(self):
        with self.app() as c:
            resp = c.get('/')

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()), {'message': 'Hello, World!'})
