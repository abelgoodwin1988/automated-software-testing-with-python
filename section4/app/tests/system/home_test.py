from unittest import TestCase
from app import app

class TestHome(TestCase):
    def test_home(self):
        app.app