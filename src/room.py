class Room:
    def __init__(self, name):

        self.name = name
        self.singers = []
        self.songs = []
        self.guests = []


    def add_guest(self, guest):

        self.guests.append(guest)


    def kick_guest_out(self, guest):

        self.guests.remove(guest)


    def add_song(self, song):

        self.songs.append(song)