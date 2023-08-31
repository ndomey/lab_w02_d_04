import unittest
from src.karaoke_bar import KaraokeBar

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):

        self.bar = KaraokeBar("Sing", 300)


    def test_bar_has_name(self):
        
        self.assertEqual("Sing", self.bar.name)


    def test_guest_has_wallet(self):
        
        self.assertEqual(300, self.bar.till)