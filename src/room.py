class Room:
    def __init__(self, name, capacity):

        self.name = name
        self.songs = []
        self.guests = []
        self.capacity = capacity


    def add_guest(self, guest):

        if len(self.guests) >= self.capacity:

            return "Sorry, this room is full."

        else:

            self.guests.append(guest)


    def kick_guest_out(self, guest):

        self.guests.remove(guest)


    def add_song(self, song):

        self.songs.append(song)


    