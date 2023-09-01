import unittest
from src.karaoke_bar import KaraokeBar
from src.guest import Guest

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):

        self.bar = KaraokeBar("Sing", 0, 5)

        self.guest_1 = Guest("Bob", 50)


    def test_bar_has_name(self):
        
        self.assertEqual("Sing", self.bar.name)


    def test_guest_has_wallet(self):
        
        self.assertEqual(0, self.bar.till)


    def test_does_wallet_reduce(self):

        self.bar.take_payment(self.guest_1) 
        self.assertEqual(5, self.bar.till)
        self.assertEqual(45, self.guest_1.wallet)