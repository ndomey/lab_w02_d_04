import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):

        self.room_1 = Room("Beatles", 2)

        self.guest_1 = Guest("Bob")
        self.guest_2 = Guest("Kate")
        self.guest_3 = Guest("Fred")

        self.song_1 = Song("BlackLilys", "Party")


    def test_room_has_name(self):

        self.assertEqual("Beatles", self.room_1.name)


    def test_can_guest_be_added_room(self):

        self.room_1.add_guest(self.guest_1)
        self.room_1.add_guest(self.guest_2)
        self.assertEqual(self.guest_1, self.room_1.guests[0])
        self.assertEqual(self.guest_2, self.room_1.guests[1])



    def test_can_guest_be_added_to_full_room(self):
 
        self.room_1.add_guest(self.guest_1)
        self.room_1.add_guest(self.guest_2)
        self.room_1.add_guest(self.guest_3)

        self.assertEqual(len(self.room_1.guests), self.room_1.capacity)



    def test_can_guest_be_kicked_out(self):

        self.room_1.add_guest(self.guest_1)
        self.room_1.kick_guest_out(self.guest_1)
        self.assertEqual(0, len(self.room_1.guests))


    def test_can_song_be_added(self):

        self.room_1.add_song(self.song_1)
        self.assertEqual(self.song_1, self.room_1.songs[0])





