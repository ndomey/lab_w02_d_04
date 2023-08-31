import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):

        self.guest_1 = Guest("Bob", 50)



    def test_guest_has_name(self):

        self.assertEqual("Bob", self.guest_1.name)


    def test_guest_has_wallet(self):
        
        self.assertEqual(50, self.guest_1.wallet)