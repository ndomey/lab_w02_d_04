import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):

        self.song_1 = Song("BlackLilys", "Party")


    def test_song_has_artist(self):

        self.assertEqual("BlackLilys", self.song_1.artist)


    def test_song_has_name(self):

        self.assertEqual("Party", self.song_1.name)
