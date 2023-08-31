import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):

        self.guest_1 = Guest("Bob")



    def test_has_name(self):

        self.assertEqual("Bob", self.guest_1.name)